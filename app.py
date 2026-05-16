from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)





@app.route("/", methods=["GET", "POST"])
def index():
    zprava = None
    tlacitko = False
    if request.method == "POST":
        sifra = request.form.get("sifra")
        if sifra.lower() == "rakev":
            zprava = "Správně! Teď něco trochu těžšího. Jak se říká žákovi z doby kamenné? "
        elif sifra.lower() == "pražák":
            zprava = "Výborně! Poslední otázka. Jak se jmenuje stránka s nejlepšími hádankami? "
        elif sifra.lower() == "blážova hádanka":
            zprava = "Odhalili jste tajemství. Teď přejděte na /tajemstvi kde vám formálně pogratuluji"
            tlacitko = True
        elif sifra == None:
            zprava = "Zadejte odpověď."
        elif len(sifra) > 30:
            zprava = "Odpověď je příliš dlouhá. Zkuste to znovu."
        else:
            zprava = "Nesprávná odpověď. Zkuste to znovu."
    return render_template("index.html", zprava=zprava, tlacitko=tlacitko)






if __name__=="__main__":
	app.run(debug=True)