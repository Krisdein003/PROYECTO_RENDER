from flask import Flask

app = Flask(__name__)

@app.route("/")
def holamundo():
    return """
    <h1>¡BIENVENIDO!</h1>
    <h2>Aplicación básica en la plataforma Render</h2>
    """

if __name__ == "__main__":
    app.run(debug=True)
