import mysql.connector

connection = mysql.connector.connect(user='devmsuser', password='devmsuser123',
                              host='155.248.231.129',
                              database='grocery_store')

cursor = connection.cursor()

product = {
    'product_name': 'pencil',
    'uom_id': '1',
    'price_per_unit': '5'
  }

query = ("INSERT INTO products "
          "(name, uom_id, price_per_unit)"
          "VALUES (%s, %s, %s)")
data = (product['product_name'], product['uom_id'], product['price_per_unit'])

cursor.execute(query, data)
connection.commit()

print(cursor.lastrowid)

connection.close()