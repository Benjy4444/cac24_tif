import mysql.connector

class Coro:

    def __init__(self, host, user, password, database):
        
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        
        self.cursor = self.conn.cursor(dictionary=True)
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS coristas (codigo INT AUTO_INCREMENT PRIMARY KEY, apellido VARCHAR(255) NOT NULL, nombre VARCHAR(255) NOT NULL, correo VARCHAR(255) NOT NULL, cuerda VARCHAR(255) NOT NULL, experiencia BOOLEAN, lectura_musical BOOLEAN, estudios_musicales BOOLEAN, activo BOOLEAN''')
        
        self.conn.commit()
        
    def agregar_corista(self, apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo):
        sql = "INSERT INTO coristas (apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo)
        
        self.cursor.execute(sql, valores)
        
        self.conn.commit()
        
        return self.cursor.lastrowid


# PROGRAMA PRINCIPAL --- PRUEBA ----
import mysql.connector

coro = Coro(host='localhost', user='root', password='',database='miapp')
# Agregamos productos a la tabla
