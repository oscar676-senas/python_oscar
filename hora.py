from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

# Endpoint para mostrar la hora actual del servidor
@app.route('/hora', methods=['GET'])
def obtener_hora():
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return jsonify({
        "hora_servidor": hora_actual
    })

if __name__ == '__main__':
    app.run(debug=True)