from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)





@app.route("/", methods=["GET", "POST"])
def index():
    zprava = None
    if request.method == "POST":
        sifra = request.form.get("sifra")
        if sifra == "rakev":
            zprava = "Správně! Teď něco trochu těžšího. Jak se říká žákovi z doby kamenné? "
        elif sifra == "pražák":
            zprava = "Výborně! Poslední otázka. Jak se jmenuje stránka s nejlepšími hádankami? "
        elif sifra == "blážova hádanka":
            zprava = "Odhalili jste tajemství. Teď přejděte na /tajemstvi kde vám formálně pogratuluji"
        else:
            zprava = "Nesprávná odpověď. Zkuste to znovu."
    return render_template("index.html", zprava=zprava)



@app.route("/tajemstvi", methods=["GET", "POST"])
def tajemstvi():
    if request.method == "POST":
        tajemstvi = request.form.get("tajemstvi")
    return render_template("tajemstvi.html")



if __name__=="__main__":
	app.run(debug=True)
