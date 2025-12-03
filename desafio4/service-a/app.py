from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def get_user():
    # Simula uma consulta ao banco
    return jsonify({"id": 1, "name": "Pedro Fernandes", "role": "Admin"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)