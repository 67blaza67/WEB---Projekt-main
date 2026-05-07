from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)





@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        zasifrovani = request.form.get("zasifrovani")
        desifrovani = request.form.get("desifrovani")
        # Zde můžete přidat logiku pro šifrování/dešifrování
    return render_template("index.html")
    



@app.route("/tajemstvi", methods=["GET", "POST"])
def tajemstvi():
    if request.method == "POST":
        tajemstvi = request.form.get("tajemstvi")
        # Zde můžete přidat logiku
    return render_template("tajemstvi.html")



if __name__=="__main__":
	app.run(debug=True)
