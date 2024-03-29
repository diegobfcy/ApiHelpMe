from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir solicitudes desde otros dominios

# Variable global para almacenar la última ubicación
last_location = {'latitude': 0.0, 'longitude': 0.0}

@app.route('/')
def index():
    return 'Hello, World!'

@app.route("/location", methods=["POST"])
def location():
    try:
        data = request.json  # Se espera que los datos se envíen en formato JSON

        # Verifica que los datos contengan 'latitude' y 'longitude'
        if 'latitude' in data and 'longitude' in data:
            latitude = data['latitude']
            longitude = data['longitude']

            # Almacena la última ubicación
            global last_location
            last_location = {'latitude': latitude, 'longitude': longitude}

            # Puedes hacer lo que quieras con la ubicación aquí
            # En este ejemplo, simplemente la devolvemos como respuesta
            response = {
                'message': 'Location received successfully',
                'latitude': latitude,
                'longitude': longitude
            }
            return jsonify(response), 200
        else:
            # Los datos no contienen los campos esperados
            return jsonify({'error': 'Invalid data'}), 400

    except Exception as e:
        # Algo salió mal al procesar la solicitud
        return jsonify({'error': str(e)}), 500

@app.route("/get_location", methods=["GET"])
def get_location():
    global last_location
    return jsonify(last_location)

if __name__ == "__main__":
    app.run(debug=True)
