from flask import Flask, request, jsonify
import products_dao
from sql_connection import get_sqs_connection

app = Flask(__name__)
connection = get_sqs_connection()

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/getProducts", methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
  print("Starting python flask server for Glocery Store Management System")
  app.run(port=5000)