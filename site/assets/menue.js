// Klappt auf schmalen Bildschirmen das Menü auf und zu.
document.addEventListener("DOMContentLoaded", function () {
  var knopf = document.querySelector(".menue-knopf");
  var nav = document.getElementById("hauptmenue");
  if (!knopf || !nav) return;
  knopf.addEventListener("click", function () {
    var offen = nav.classList.toggle("offen");
    knopf.setAttribute("aria-expanded", offen ? "true" : "false");
  });
});
