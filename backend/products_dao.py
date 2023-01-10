# dao - data access object
# Driver - is a python module allows you to connect MySQL database

from sql_connection import get_sqs_connection

def get_all_products(connection):
  cursor = connection.cursor()

  query = ("SELECT products.product_id,products.name,products.uom_id, uom.uom_name,products.price_per_unit " 
          "FROM products INNER JOIN uom ON products.uom_id = uom.uom_id")

  cursor.execute(query)

  response = []

  for (product_id,name,uom_id,uom_name,price_per_unit) in cursor:
    response.append(
      {
        'product_id': product_id,
        'name': name,
        'uom_id': uom_id,
        'uom_name': uom_name,
        'price_per_unit': price_per_unit
      }
    )

  return response

def insert_new_product(connection, product):
  cursor = connection.cursor()

  query = ("INSERT INTO products "
          "(name, uom_id, price_per_unit) VALUES (%s,%s,%s)")

  data = (product['product_name'], product['uom_id'], product['price_per_unit'] )
  
  # Insert
  cursor.execute(query, data)
  # commit to the database
  connection.commit()

  return cursor.lastrowid

def delete_product(connection, product_id):
  cursor = connection.cursor()

  query = ("DELETE FROM products WHERE product_id=" + str(product_id))

  cursor.execute(query)
  connection.commit()

  return cursor.lastrowid

# make the code moduler
if __name__=='__main__':
  connection = get_sqs_connection()
  # print(get_all_products(connection))
  # print(insert_new_product(connection, {
  #   'product_name': 'crbook80page',
  #   'uom_id': '1',
  #   'price_per_unit': '80'
  # }))
  # print(delete_product(connection, 4))
