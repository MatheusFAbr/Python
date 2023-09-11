from flask import render_template

def init_app(app):
    @app.route("/")
    def index():
        universo = "marvel"
        heroi = "hulkao"
        return render_template("index.html", **locals())