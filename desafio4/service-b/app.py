import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/profile')
def get_profile():
    # Aqui acontece a mágica: chamamos o outro container pelo NOME
    try:
        response = requests.get('http://service-a:5000/users')
        user_data = response.json()

        # Adiciona dados extras
        user_data['active_since'] = '2024'
        user_data['status'] = 'Online'

        return jsonify(user_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)