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

class Coro:
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
    
    def listar_coristas(self):
        self.cursor.execute("SELECT * FROM coristas")
        coristas = self.cursor.fetchall()
        return coristas
    
    def consultar_corista(self, codigo):
        self.cursor.execute(f"SELECT * FROM coristas WHERE codigo = {codigo}")
        return self.cursor.fetchone()
    
    def mostrar_corista(self, codigo):
        corista = self.consultar_corista(codigo)
        if corista:
            print("-" * 40)
            print(f"Código............: {corista['codigo']}")
            print(f"Apellido..........: {corista['apellido']}")
            print(f"Nombre............: {corista['nombre']}")
            print(f"Correo............: {corista['correo']}")
            print(f"Cuerda............: {corista['cuerda']}")
            print(f"Experiencia.......: {corista['experiencia']}")
            print(f"Lectura Musical...: {corista['lectura_musical']}")
            print(f"Estudios musicales: {corista['estudios_musicales']}")
            print(f"Activo............: {corista['activo']}")
            print("-" * 40)
        else:
            print("Corista no encontrado.")
    
    def agregar_corista(self, apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo):
        sql = "INSERT INTO coristas (apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def modificar_corista(self, mod_codigo, nuevo_apellido, nuevo_nombre, nuevo_correo, nueva_cuerda, nueva_experiencia, nueva_lectura_musical, nuevo_estudios_musicales, nuevo_activo):
        sql = f"UPDATE coristas SET apellido= %s, nombre= %s, correo= %s, cuerda= %s, experiencia= %s, lectura_musical= %s, estudios_musicales= %s, activo= %s WHERE codigo = {mod_codigo}"
        valores = (nuevo_apellido, nuevo_nombre, nuevo_correo, nueva_cuerda, nueva_experiencia, nueva_lectura_musical, nuevo_estudios_musicales, nuevo_activo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def eliminar_corista(self, codigo):
        self.cursor.execute(f"DELETE FROM coristas WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0

    
        
        
#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------

# Crear una instancia de la clase Catalogo
coro = Coro(host='localhost', user='root', password='',database='miapp')

# Carpeta para guardar las imagenes
ruta_destino = './static/imagenes/'

@app.route("/coristas", methods=["GET"])
def listar_coristas():
    coristas = coro.listar_coristas()
    return jsonify(coristas)

@app.route("/coristas/<int:codigo>", methods=["GET"])
def mostrar_corista(codigo):
    corista = coro.consultar_corista(codigo)
    if corista:
        return jsonify(corista)
    else:
        return "Corista no encontrado", 404
    
@app.route("/coristas", methods=["POST"])
def agregar_corista():
    #Recojo los datos del form
    apellido = request.form['apellido']
    nombre = request.form['nombre']
    correo = request.form['correo']
    cuerda = request.form['cuerda']
    experiencia = request.form['experiencia']
    lectura_musical = request.form['lectura_musical']
    estudios_musicales = request.form['estudios_musicales']
    activo = request.form['activo']    
    #nombre_imagen=""
    # Genero el nombre de la imagen
    #nombre_imagen = secure_filename(imagen.filename)
    #nombre_base, extension = os.path.splitext(nombre_imagen)
    #nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
    nuevo_codigo = coro.agregar_corista(apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo)
    if nuevo_codigo:
        #imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))
        return jsonify({"mensaje": "Corista agregado correctamente.","codigo": nuevo_codigo, "apellido": apellido}), 201
    else:
        return jsonify({"mensaje": "Error al agregar el corista."}), 500
    
@app.route("/coristas/<int:codigo>", methods=["PUT"])
def modificar_corista(codigo):
    #Se recuperan los nuevos datos del formulario
    nuevo_apellido = request.form['apellido']
    nuevo_nombre = request.form['nombre']
    nuevo_correo = request.form['correo']
    nueva_cuerda = request.form['cuerda']
    nueva_experiencia = request.form['experiencia']
    nueva_lectura_musical = request.form['lectura_musical']
    nuevo_estudios_musicales = request.form['estudios_musicales']
    nuevo_activo = request.form['activo']    
    # Verifica si se proporcionó una nueva imagen
    #if 'imagen' in request.files:
        #imagen = request.files['imagen']
        # Procesamiento de la imagen
        #nombre_imagen = secure_filename(imagen.filename)
        #nombre_base, extension = os.path.splitext(nombre_imagen)
        #nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
        # Guardar la imagen en el servidor
        #imagen.save(os.path.join(RUTA_DESTINO, nombre_imagen))
    # Busco el producto guardado
    corista = coro.consultar_corista(codigo)
    #if corista: # Si existe el producto...
        #imagen_vieja = producto["imagen_url"]
        # Armo la ruta a la imagen
        #ruta_imagen = os.path.join(RUTA_DESTINO, imagen_vieja)
        # Y si existe la borro.
        #if os.path.exists(ruta_imagen):
        #os.remove(ruta_imagen)
    #else:
        #producto = catalogo.consultar_producto(codigo)
        #if producto:
            #nombre_imagen = producto["imagen_url"]
    # Se llama al método modificar_producto pasando el codigo del producto y los nuevos datos.
    if coro.modificar_corista(codigo, nuevo_apellido, nuevo_nombre, nuevo_correo, nueva_cuerda, nueva_experiencia, nueva_lectura_musical, nuevo_estudios_musicales, nuevo_activo):
        return jsonify({"mensaje": "Corista modificado"}), 200
    else:
        return jsonify({"mensaje": "Corista no encontrado"}), 403

@app.route("/coristas/<int:codigo>", methods=["DELETE"])
def eliminar_corista(codigo):
    # Primero, obtén la información del producto para encontrar la imagen
    corista = coro.consultar_corista(codigo)
    if corista:
        # Eliminar la imagen asociada si existe
        #ruta_imagen = os.path.join(ruta_destino, producto['imagen_url'])
        #if os.path.exists(ruta_imagen):
            #os.remove(ruta_imagen)
        # Luego, elimina el producto del catálogo
        if coro.eliminar_corista(codigo):
            return jsonify({"mensaje": "Corista eliminado"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el corista"}), 500
    else:
        return jsonify({"mensaje": "Corista no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)