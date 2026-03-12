from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():

    valor_digitado = request.args.get("moeda")

    preco_usd = None
    preco_brl = None

    if valor_digitado:

        url = f"https://api.coingecko.com/api/v3/simple/price?ids={valor_digitado}&vs_currencies=usd,brl"

        resposta = requests.get(url)
        dados = resposta.json()

        if valor_digitado in dados:
            preco_usd = f"{dados[valor_digitado]['usd']:,.2f}"
            preco_brl = f"{dados[valor_digitado]['brl']:,.2f}".replace(",","x").replace(".", ",").replace("x",".")
        
        if valor_digitado not in dados:
            preco_usd = "Moeda não encontrada!"
            preco_brl = "Moeda não encontrada!"

    return render_template("index.html", moeda=valor_digitado, preco_usd=preco_usd, preco_brl=preco_brl)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))