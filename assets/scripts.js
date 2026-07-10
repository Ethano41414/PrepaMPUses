let nombre_clicks=0;

const bouton_actualiseur=document.getElementById("hided_button");
if (bouton_actualiseur) {
bouton_actualiseur.addEventListener("click",function() {
    nombre_clicks++;
    if (4>nombre_clicks && nombre_clicks>=3) {
        bouton_actualiseur.textContent="Actualiser";
        bouton_actualiseur.style.opacity="1";
        bouton_actualiseur.style.width="6rem";
    };
    if (nombre_clicks>=4) {
        bouton_actualiseur.textContent="Act";
    }
});}
