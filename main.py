from codecarbon import OfflineEmissionsTracker

from flask import jsonify

from app import app
from model import CalculFonction



@app.route("/")
def index():
    return "Hello world !"

@app.route("/home")
def home():
    return jsonify({'msg': 'Bienvenue'})

@app.route("/donnee")
def donnee():
    p = CalculFonction(15, 25, 25, 15, 30)
    # valeur = p.Calcul()
    tracker = OfflineEmissionsTracker(country_iso_code="FRA")
    tracker.start()
    valeur2 = p.Calculboucle()
    tracker.stop()
    # for i in (p.Calculboucle):
    #     print(i)
    # return jsonify({"Temperature ":p.I, "Calcul":p.Calcul(), "Boucle":p.Calculboucle()})
    return jsonify(valeur2)

@app.route("/carbone")
def carbone():
    p = CalculFonction(15, 12, 13, 15, 15)
    # valeur = p.Calcul()
    tracker = OfflineEmissionsTracker(country_iso_code="FRA")
    tracker.start()
    valeur2 = p.Calculboucle()
    tracker.stop()
    # for i in (p.Calculboucle):
    #     print(i)
    # return jsonify({"Temperature ":p.I, "Calcul":p.Calcul(), "Boucle":p.Calculboucle()})
    return jsonify(tracker.final_emissions_data.emissions, tracker.final_emissions_data.cpu_energy,tracker.final_emissions_data.ram_energy)

if __name__ == "__main__":
    app.run()