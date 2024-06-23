#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify
# Instalar con pip install flask-cors
from flask_cors import CORS
# Instalar con pip install mysql-connector-python
import mysql.connector
# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename
# No es necesario instalar, es parte del sistema standard de Python
import os
import time
#--------------------------------------------------------------------

app = Flask(__name__)
CORS(app) # Esto habilitará CORS para todas las rutas

class Catalogo:
#----------------------------------------------------------------
# Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(host=host, user=user, password=password)
        self.cursor = self.conn.cursor()
        
        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
            
            
            # Una vez que la base de datos está establecida, creamos la tabla si no existe
            #self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (codigo INT AUTO_INCREMENT PRIMARY KEY, descripcion VARCHAR(255) NOT NULL, cantidad INT NOT NULL, precio DECIMAL(10, 2) NOT NULL, imagen_url VARCHAR(255), proveedor INT(4))''')
            self.conn.commit()
            # Cerrar el cursor inicial y abrir uno nuevo con el parámetro
            dictionary=True
            self.cursor.close()
            self.cursor = self.conn.cursor(dictionary=True)
        
        
        
#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------

# Crear una instancia de la clase Catalogo
catalogo = Catalogo(host='localhost', user='root', password='',database='miapp')

# Carpeta para guardar las imagenes
ruta_destino = './static/imagenes/'

