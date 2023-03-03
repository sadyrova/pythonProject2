import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)

    return connection

def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(conn, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity) 
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def select_products_by_price_limit(conn, limit):
    try:
        sql = '''SELECT * FROM products WHERE price <= ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

def update_product(conn, product):
    try:
        sql = '''UPDATE products SET price = ?
        WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_quantity(conn, product):
    try:
        sql = '''UPDATE products SET quantity = ?
        WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, id):
     try:
         sql = '''DELETE FROM products WHERE id = ?'''
         cursor = conn.cursor()
         cursor.execute(sql, (id,))
         conn.commit()
     except sqlite3.Error as e:
         print(e)

sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL, 
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER NOT NULL DEFAULT 0
)
'''
connection = create_connection('hw.db')
if connection is not None:
    print('Connected successfully')
    # create_table(connection, sql_create_products_table)
    insert_product(connection, ("milk", 77.12, 100))
    insert_product(connection, ("cheese", 378.22, 110))
    insert_product(connection, ("tea", 98.25, 120))
    insert_product(connection, ("oil", 150.20, 130))
    insert_product(connection, ("cream", 277.22, 140))
    insert_product(connection, ("sugar", 95.35, 150))
    insert_product(connection, ("salt", 25.12, 160))
    insert_product(connection, ("chocolate", 500.32, 170))
    insert_product(connection, ("coffee", 515.25, 180))
    insert_product(connection, ("tomato", 47.62, 190))
    insert_product(connection, ("ketchup", 77.40, 200))
    insert_product(connection, ("yoghut", 60.10, 210))
    insert_product(connection, ("rice", 190.25, 220))
    insert_product(connection, ("flour", 58.45, 230))
    insert_product(connection, ("pasta", 50.20, 240))

    # select_all_products(connection)
    # select_products_by_price_limit(connection, 100)
    # delete_product(connection, 3)
    # update_product_quantity(connection, (500,  2))
    print('DONE')
    connection.close()