from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my phone server!"

@app.route("/status")
def status():
    return jsonify({
        "status": "running",
        "device": "Mi A2",
        "server": "Flask on Termux"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
