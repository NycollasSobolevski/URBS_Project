import pyodbc
from Secrets import secretos as sc

def connection():
    conn = pyodbc.connect('DRIVER='+sc.driver+';SERVER='+sc.server+';DATABASE='+sc.database+';Trusted_Connection=yes;')
    cursor = conn.cursor()
    return cursor

def search(table, item='*'):
    cursor = connection()
    cursor.execute(f'SELECT {item} FROM {table}')
    # res = []
    # for row in cursor.fechall():
    #     res.append(row)
    return cursor.fetchall()

def insert(table, data):
    cursor = connection()
    cursor.execute(f'INSERT INTO {table} VALUES ({data})')
    cursor.commit()
    print(f"{data} ------- Inserted")

def delete(table, data):
    cursor = connection()
    cursor.execute(f'DELETE FROM {table} WHERE {data} ')
    cursor.commit()
    print(f'{data} ------- Deleted')

