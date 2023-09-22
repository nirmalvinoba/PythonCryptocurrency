from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template ("home.html")

@app.route('/bitcoins', methods = ["GET","POST"])
def coins():
    if request.method == "POST":
        coin = request.form.get("coin")
        crypto_currency =  requests.get("http://api.coinlayer.com/live?access_key=1948b358ce3ead0a236e3545f561ca5e")

        success = crypto_currency.json().get("success")
        target = crypto_currency.json().get("target")
        rate=crypto_currency.json().get("rates")
        if coin in rate:
            data=rate.get(coin)

        return render_template ("index.html",box=data,success=success,target=target,coin=coin)
    return render_template ("index.html")


if __name__ == "__main__":
    app.run(debug=True)






