import mysql.connector

class Coro:

    def __init__(self, host, user, password, database):
        
        self.conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
        
        self.cursor = self.conn.cursor(dictionary=True)
        
        #No funcionó la creación de la tabla que sigue. Lo hice directamente desde un script en Postgres
        #self.cursor.execute('''CREATE TABLE IF NOT EXISTS coristas (codigo INT AUTO_INCREMENT PRIMARY KEY, apellido VARCHAR(255) NOT NULL, nombre VARCHAR(255) NOT NULL, correo VARCHAR(255) NOT NULL, cuerda VARCHAR(255) NOT NULL, experiencia BOOLEAN, lectura_musical BOOLEAN, estudios_musicales BOOLEAN, activo BOOLEAN''')
        
        self.conn.commit()
        
    def agregar_corista(self, apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo):
        sql = "INSERT INTO coristas (apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo)
        
        self.cursor.execute(sql, valores)
        
        self.conn.commit()
        
        return self.cursor.lastrowid
    
    # Consultamos un producto a partir de su código
    def consultar_corista(self, codigo):
        self.cursor.execute(f"SELECT * FROM coristas WHERE codigo = {codigo}")
        return self.cursor.fetchone()

    # Modificamos un producto a partir de su código
    def modificar_corista(self, mod_codigo, nuevo_apellido, nuevo_nombre, nuevo_correo, nueva_cuerda, nueva_experiencia, nueva_lectura_musical, nuevo_estudios_musicales, nuevo_activo):
        sql = f"UPDATE coristas SET apellido= %s, nombre= %s, correo= %s, cuerda= %s, experiencia= %s, lectura_musical= %s, estudios_musicales= %s, activo= %s WHERE codigo = {mod_codigo}"
        valores = (nuevo_apellido, nuevo_nombre, nuevo_correo, nueva_cuerda, nueva_experiencia, nueva_lectura_musical, nuevo_estudios_musicales, nuevo_activo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    # Mostramos los datos de un producto a partir de su código
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
            
    def listar_coristas(self):
        self.cursor.execute("SELECT * FROM coristas")
        coristas = self.cursor.fetchall()
        return coristas
    
    # Eliminamos un producto de la tabla a partir de su código
    def eliminar_corista(self, codigo):
        self.cursor.execute(f"DELETE FROM coristas WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0
            
            
            
            

# PROGRAMA PRINCIPAL --- PRUEBA ----
import mysql.connector

coro = Coro(host='localhost', user='root', password='',database='miapp')
# Agregamos productos a la tabla
#coro.agregar_corista("pepellido", "nombre", "correo", "cuerda", "experiencia", "lectura_musical", "estudios_musicales", "activo")
#coro.agregar_corista("pepe", "nombre", "correo", "cuerda", "experiencia", "lectura_musical", "estudios_musicales", "activo")
#coro.agregar_corista("llido", "nombre", "correo", "cuerda", "experiencia", "lectura_musical", "estudios_musicales", "activo")
#coro.agregar_corista("lastname", "name", "mail", "chord", "experiencia", "lectura_musical", "estudios_musicales", "activo")

 # Consultamos un producto y lo mostramos
#cod_cor = int(input("Ingrese el código del corista: "))
#corista = coro.consultar_corista(cod_cor)
#if corista:
#   print(f"Corista encontrado: {corista['codigo']} - {corista['apellido']}")
#else:
#   print(f'Corista {cod_cor} no encontrado.')
    
# Modificamos un corista y lo mostramos
#coro.mostrar_corista(20)
#coro.modificar_corista(20, "eeeeeeeeeeeeeee", "mail", "chord", "XP", "lectura", "estudios", "activo","qqqq")
#coro.mostrar_corista(21)

# Listamos todos los productos
#coristas = coro.listar_coristas()
#for corista in coristas:
#    print(corista)
    
# Eliminamos un producto
#coro.eliminar_corista(19)
#coristas = coro.listar_coristas()
#for corista in coristas:
#    print(corista)