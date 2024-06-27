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
CORS(app)  # Esto habilitará CORS para todas las rutas

class Coro:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None
        self.connect_to_db()

    def connect_to_db(self):
        self.conn = mysql.connector.connect(
            host=self.host, 
            user=self.user, 
            password=self.password
        )
        self.cursor = self.conn.cursor(dictionary=True)
        
        try:
            self.cursor.execute(f"USE {self.database}")
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {self.database}")
                self.conn.database = self.database
            else:
                raise err
            self.conn.commit()

    def close_db(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def listar_coristas(self):
        self.cursor.execute("SELECT * FROM coristas")
        return self.cursor.fetchall()

    def consultar_corista(self, codigo):
        self.cursor.execute("SELECT * FROM coristas WHERE codigo = %s", (codigo,))
        return self.cursor.fetchone()

    def agregar_corista(self, apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo):
        sql = """
            INSERT INTO coristas 
            (apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid

    def modificar_corista(self, codigo, apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo):
        sql = """
            UPDATE coristas SET 
            apellido = %s, nombre = %s, correo = %s, cuerda = %s, experiencia = %s, 
            lectura_musical = %s, estudios_musicales = %s, activo = %s 
            WHERE codigo = %s
        """
        valores = (apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def eliminar_corista(self, codigo):
        self.cursor.execute("DELETE FROM coristas WHERE codigo = %s", (codigo,))
        self.conn.commit()
        return self.cursor.rowcount > 0


#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------

# Crear una instancia de la clase Coro
coro = Coro(host='localhost', user='root', password='', database='miapp')

@app.route("/coristas", methods=["GET"])
def listar_coristas():
    try:
        coristas = coro.listar_coristas()
        return jsonify(coristas), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/coristas/<int:codigo>", methods=["GET"])
def mostrar_corista(codigo):
    try:
        corista = coro.consultar_corista(codigo)
        if corista:
            return jsonify(corista), 200
        else:
            return jsonify({"mensaje": "Corista no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/coristas", methods=["POST"])
def agregar_corista():
    try:
        apellido = request.form['apellido']
        nombre = request.form['nombre']
        correo = request.form['correo']
        cuerda = request.form['cuerda']
        experiencia = request.form['experiencia']
        lectura_musical = request.form['lectura_musical']
        estudios_musicales = request.form['estudios_musicales']
        activo = request.form['activo']
        
        nuevo_codigo = coro.agregar_corista(apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo)
        return jsonify({"mensaje": "Corista agregado correctamente", "codigo": nuevo_codigo, "apellido": apellido}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/coristas/<int:codigo>", methods=["PUT"])
def modificar_corista(codigo):
    try:
        apellido = request.form['apellido']
        nombre = request.form['nombre']
        correo = request.form['correo']
        cuerda = request.form['cuerda']
        experiencia = request.form['experiencia']
        lectura_musical = request.form['lectura_musical']
        estudios_musicales = request.form['estudios_musicales']
        activo = request.form['activo']
        
        if coro.modificar_corista(codigo, apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo):
            return jsonify({"mensaje": "Corista modificado"}), 200
        else:
            return jsonify({"mensaje": "Corista no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/coristas/<int:codigo>", methods=["DELETE"])
def eliminar_corista(codigo):
    try:
        if coro.eliminar_corista(codigo):
            return jsonify({"mensaje": "Corista eliminado"}), 200
        else:
            return jsonify({"mensaje": "Corista no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    try:
        app.run(debug=True)
    finally:
        coro.close_db()
