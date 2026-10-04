import json, math

R = 6371008.8
LAT0 = 49.62


def xy(lat, lon):
    return ((lon - 9.65) * math.cos(math.radians(LAT0)) * math.pi / 180 * R, (lat - LAT0) * math.pi / 180 * R)


def ll(x, y):
    return (LAT0 + y / R * 180 / math.pi, 9.65 + x / (math.cos(math.radians(LAT0)) * math.pi / 180 * R))


class Linie:
    def __init__(self, coords):
        self.pts = [xy(c[1], c[0]) for c in coords]
        self.cum = [0.0]
        for a, b in zip(self.pts, self.pts[1:]):
            self.cum.append(self.cum[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
        self.laenge = self.cum[-1]

    def projiziere(self, lat, lon):
        px, py = xy(lat, lon)
        best = (1e18, 0.0)
        for i in range(len(self.pts) - 1):
            ax, ay = self.pts[i]
            bx, by = self.pts[i + 1]
            dx, dy = bx - ax, by - ay
            l2 = dx * dx + dy * dy
            t = 0 if l2 == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / l2))
            qx, qy = ax + t * dx, ay + t * dy
            d = math.hypot(px - qx, py - qy)
            if d < best[0]:
                best = (d, self.cum[i] + t * math.sqrt(l2))
        return best  # (Abstand zur Linie, s)

    def punkt(self, s):
        s = max(0, min(self.laenge, s))
        for i in range(len(self.pts) - 1):
            if self.cum[i + 1] >= s:
                l = self.cum[i + 1] - self.cum[i]
                t = 0 if l == 0 else (s - self.cum[i]) / l
                a, b = self.pts[i], self.pts[i + 1]
                return ll(a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1]))
        return ll(*self.pts[-1])


def lade(pfad):
    g = json.load(open(pfad, encoding="utf-8"))
    return [Linie(f["geometry"]["coordinates"]) for f in g["features"]]
