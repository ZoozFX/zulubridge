from flask import Flask, jsonify
from scrape_zulu import get_latest_trades

app = Flask(__name__)

@app.route('/trades')
def trades():
    data = get_latest_trades()
    return jsonify(data)

if __name__ == "__main__":
    app.run()
