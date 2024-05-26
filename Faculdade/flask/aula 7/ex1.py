from flask import Flask

app = Flask (__name__)

@app.route("/")
@app.route("/bom-dia")
def bom_dia():
    return "Bom dia!"

@app.route("/boa-tarde")
def boa_tarde():
    return "Boa Tarde!"

@app.route("/boa-noite")
def boa_noite():
    return "Boa Noite!"

@app.route("/um/caminho/com/varios/elementos")
def oi_pessoal():
    return "Oi pessoal"

if __name__ == "__main__":
    app.run(host = "localhost", port = 5002, debug = True) 