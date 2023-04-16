from flask import render_template
import connexion
import config
from models import Character

app = config.connex_app
app.add_api(config.basedir / "swagger.yml", options={
        'swagger_ui': False
    })

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/documentation")
def documentation():
    return render_template("documentation.html")

@app.route("/swagger.yml")
def swagger():
    return render_template("swagger.yml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)