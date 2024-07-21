# IP Adress = your PC's IP
# Port = 8080

from flask import Flask, request, jsonify
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)

@app.route("/",methods=['GET'])
def home():
    response_data = {'status': 'success'}
    return response_data

@app.route("/Workcell_Logging", methods=['POST'])
def Workcell_Logging():
    data = request.get_data()
    print(data)
    response_data = {'status': 'success'}
    return jsonify(response_data), 200

if __name__ == '__main__':
    local_ip = socket.gethostbyname(socket.gethostname())
    print(f"Running on {local_ip}:1234")
    app.run('0.0.0.0', debug=True, port=8080, ssl_context='adhoc')
