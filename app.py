from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)





@app.route("/", methods=["GET", "POST"])
def index():
    zprava = None
    if request.method == "POST":
        sifra = request.form.get("sifra")
        if sifra == "Blážova šifra":
            zprava = "Gratulujeme! Odhalili jste tajemství. Teď misto index.html přejděte na tajemstvi kde vám formálně pogratuluji"
        else:
            zprava = "Nesprávná šifra. Zkuste to znovu."
    return render_template("index.html", zprava=zprava)



@app.route("/tajemstvi", methods=["GET", "POST"])
def tajemstvi():
    if request.method == "POST":
        tajemstvi = request.form.get("tajemstvi")
        # Zde můžete přidat logiku
    return render_template("tajemstvi.html")



if __name__=="__main__":
	app.run(debug=True)
