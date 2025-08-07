from flask import Flask, request, jsonify

app = Flask(__name__)

# تخزين الصفقات في الذاكرة (يُحذف عند إعادة التشغيل)
stored_trades = []

@app.route("/")
def home():
    return jsonify({"message": "ZuluBridge API is running."})

@app.route("/trades", methods=["GET"])
def get_trades():
    return jsonify(stored_trades)

@app.route("/update_trades", methods=["POST"])
def update_trades():
    global stored_trades
    try:
        data = request.get_json()
        if not isinstance(data, list):
            return jsonify({"error": "Expected a list of trades"}), 400

        stored_trades = data
        return jsonify({"message": "Trades updated successfully", "count": len(data)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
