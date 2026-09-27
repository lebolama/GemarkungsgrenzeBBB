const CACHE_VERSION = "grenzgaenge-v2";
const APP_CACHE = `${CACHE_VERSION}-app`;
const TILE_CACHE = `${CACHE_VERSION}-tiles`;

const OFFLINE_ASSETS = [
  "./standorte.html",
  "./data.json",
  "./standorte-positionen.json",
  "./Gemarkungsgrenze Tauberbischofsheim.geojson",
  "./Flurnamen/flurnamen.json",
  "./Flurnamen/pois.txt",
  "./Flurnamen/gemarkungskarte-1932.jpg",
  "./Flurnamen/dgk5-tauberbischofsheim.jpg",
  "https://unpkg.com/leaflet/dist/leaflet.css",
  "https://unpkg.com/leaflet/dist/leaflet.js",
  "https://unpkg.com/leaflet/dist/images/layers.png",
  "https://unpkg.com/leaflet/dist/images/layers-2x.png"
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(APP_CACHE)
      .then((cache) => cache.add("./standorte.html"))
      .catch(() => undefined)
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys
          .filter((key) => key.startsWith("grenzgaenge-") && ![APP_CACHE, TILE_CACHE].includes(key))
          .map((key) => caches.delete(key))
      ))
      .then(() => self.clients.claim())
  );
});

async function notifyClients(message) {
  const clients = await self.clients.matchAll({ type: "window", includeUncontrolled: true });
  clients.forEach((client) => client.postMessage(message));
}

async function cacheOfflinePackage() {
  const cache = await caches.open(APP_CACHE);
  let assets = OFFLINE_ASSETS;
  try {
    const poiResponse = await fetch("./Flurnamen/pois.txt", { cache: "reload" });
    const poiText = await poiResponse.text();
    const photoAssets = poiText
      .split(/\r?\n/)
      .map((line) => line.match(/^\s+Foto:\s*([^|]+?)(?:\s*\|.*)?$/i)?.[1]?.trim())
      .filter((file) => file && /^[^\\/:*?"<>|]+\.(?:jpe?g|png|webp)$/i.test(file))
      .map((file) => `./Flurnamen/poi-bilder/${encodeURIComponent(file)}`);
    assets = [...new Set([...OFFLINE_ASSETS, ...photoAssets])];
  } catch {
    assets = OFFLINE_ASSETS;
  }
  let done = 0;
  const failures = [];
  for (const asset of assets) {
    try {
      const request = new Request(asset, { cache: "reload" });
      const response = await fetch(request);
      if (!response.ok && response.type !== "opaque") throw new Error(`HTTP ${response.status}`);
      await cache.put(request, response);
    } catch (error) {
      failures.push(`${asset}: ${error.message}`);
    }
    done += 1;
    await notifyClients({ type: "OFFLINE_PROGRESS", done, total: assets.length });
  }
  if (failures.length) {
    await notifyClients({
      type: "OFFLINE_ERROR",
      message: `${failures.length} Datei${failures.length === 1 ? "" : "en"} konnten nicht gespeichert werden.`
    });
  } else {
    await notifyClients({ type: "OFFLINE_COMPLETE" });
  }
}

self.addEventListener("message", (event) => {
  if (event.data?.type === "CACHE_OFFLINE_PACKAGE") {
    event.waitUntil(cacheOfflinePackage());
  }
});

async function trimCache(cacheName, maximumEntries) {
  const cache = await caches.open(cacheName);
  const keys = await cache.keys();
  await Promise.all(keys.slice(0, Math.max(0, keys.length - maximumEntries)).map((key) => cache.delete(key)));
}

async function networkFirst(request) {
  const cache = await caches.open(APP_CACHE);
  try {
    const response = await fetch(request);
    if (response.ok || response.type === "opaque") await cache.put(request, response.clone());
    return response;
  } catch (error) {
    const cached = await cache.match(request);
    if (cached) return cached;
    if (request.mode === "navigate") {
      const fallback = await cache.match("./standorte.html");
      if (fallback) return fallback;
    }
    throw error;
  }
}

async function cacheFirst(request, cacheName, maximumEntries = null) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request);
  if (cached) return cached;
  const response = await fetch(request);
  if (response.ok || response.type === "opaque") {
    await cache.put(request, response.clone());
    if (maximumEntries) await trimCache(cacheName, maximumEntries);
  }
  return response;
}

self.addEventListener("fetch", (event) => {
  const { request } = event;
  if (request.method !== "GET") return;
  const url = new URL(request.url);
  const isOsmTile = /(^|\.)tile\.openstreetmap\.org$/.test(url.hostname);
  const isLeafletAsset = url.hostname === "unpkg.com";
  const isLocalImage = url.origin === self.location.origin && /\.(?:jpg|jpeg|png|webp)$/i.test(url.pathname);

  if (isOsmTile) {
    event.respondWith(cacheFirst(request, TILE_CACHE, 800));
  } else if (isLeafletAsset || isLocalImage) {
    event.respondWith(cacheFirst(request, APP_CACHE));
  } else if (url.origin === self.location.origin || request.mode === "navigate") {
    event.respondWith(networkFirst(request));
  }
});
