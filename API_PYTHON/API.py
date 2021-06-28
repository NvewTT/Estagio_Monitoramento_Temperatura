from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
from SQL_CONECT import connect,GetDados
app = Flask(__name__)
CORS(app)

@app.route('/sensor/<string:pesquisa>', methods = ['GET'])
def PostSensor1(pesquisa):
    connect(pesquisa.split("&"))
    return "s"

@app.route('/sensor_banco/<string:pesquisa>', methods = ['GET'])
def GetBanco(pesquisa):
    return GetDados(pesquisa)
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")  