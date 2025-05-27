from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(
            host='db',
            user='user',
            password='password',
            database='mydb'
        )
        return "Conexión exitosa con la base de datos MySQL!"
    except Exception as e:
        return f"Error al conectar con la base de datos: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
