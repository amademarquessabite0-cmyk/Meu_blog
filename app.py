from flask import Flask, render_template
import os

# Cria o app Flask
app = Flask(__name__)

# Rota principal
@app.route("/")
def index():
    return render_template("index.html")

# Inicia o servidor
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
