from flask import Flask, make_response, jsonify
from bd import Cars


app = Flask(__name__)


@app.route('/cars', methods=['GET'])
def get_cars():
    return make_response(
        jsonify(Cars)
    )




app.run()