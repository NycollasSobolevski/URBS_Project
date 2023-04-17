import pyodbc
from Secrets import secretos as sc

def connection():
    conn = pyodbc.connect('DRIVER='+sc.driver+';SERVER='+sc.server+';DATABASE='+sc.database+';Trusted_Connection=yes;')
    cursor = conn.cursor()
    return cursor

def search(table, item='*'):
    cursor = connection()
    cursor.execute(f'SELECT {item} FROM {table}')

def insert(table, data):
    cursor = connection()
    cursor.execute(f'INSERT INTO {table} VALUES ({data})')

def delete(table, data):
    cursor = connection()
    cursor.execute(f'DELETE {table} WHERE={data} ')