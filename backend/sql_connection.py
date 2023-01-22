import mysql.connector

__cnx = None

def get_sqs_connection():
  global __cnx
  if __cnx is None:
    __cnx = mysql.connector.connect(user='devmsuser', password='devmsuser123', host='155.248.231.129',database='grocery_store')
  
  return __cnx