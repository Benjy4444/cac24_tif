# Definimos una lista de diccionarios para almacenar los coristas.
coristas = []

# Función para consultar si existe un corista, y en caso negativo, se lo agrega a la BD
def agregar_corista(codigo, apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo):
    if consultar_corista(codigo):
        return False
    nuevo_corista = {
        'codigo': codigo,
        'apellido': apellido,
        'nombre': nombre,
        'correo': correo,
        'cuerda': cuerda,
        'experiencia': experiencia,
        'lectura_musical': lectura_musical,
        'estudios_musicales': estudios_musicales,
        'activo': activo
    }
    coristas.append(nuevo_corista)
    return True

# Función para consultar datos de coristas
def consultar_corista(codigo):
    for corista in coristas:
        if corista['codigo'] == codigo:
            return corista
    return False

# Función para modificar datos de coristas
def modificar_corista(codigo, nuevo_apellido, nuevo_nombre, nuevo_correo, nueva_cuerda, nueva_experiencia, 
                       nueva_lectura_musical, nuevo_estudios_musicales, nuevo_activo):
    for corista in coristas:
        if corista['codigo'] == codigo:
            corista['apellido'] = nuevo_apellido
            corista['nombre'] = nuevo_nombre
            corista['correo'] = nuevo_correo
            corista['nueva_cuerda'] = nueva_cuerda
            corista['experiencia'] = nueva_experiencia
            corista['lectura_musical'] = nueva_lectura_musical
            corista['estudios_musicales'] = nuevo_estudios_musicales
            corista['activo'] = nuevo_activo                   
            return True
    return False

# Función para listar coristas
def listar_coristas():
    print("-" * 50)
    for corista in coristas:
        print(f"Código............: {corista['codigo']}")
        print(f"Apellido..........: {corista['apellido']}")
        print(f"Nombre............: {corista['nombre']}")
        print(f"Correo............: {corista['correo']}")
        print(f"Cuerda............: {corista['cuerda']}")
        print(f"Experiencia.......: {corista['experiencia']}")
        print(f"Lectura Musical...: {corista['lectura_musical']}")
        print(f"Estudios musicales: {corista['estudios_musicales']}")
        print(f"Activo............: {corista['activo']}")
        print("-" * 50)

# Función para eliminar un corista
def eliminar_corista(codigo):
    for corista in coristas:
        if corista['codigo'] == codigo:
            coristas.remove(corista)
            return True
    return False

# PRUEBAS --------------------------------------------------
# Agregamos productos a la lista:
agregar_corista(1, "apellido", "nombre", "correo", "cuerda", "experiencia", "lectura_musical", "estudios_musicales", "activo")
agregar_corista(2, "lastname", "firstname", "correo", "cuerda", "experiencia", "lectura_musical", "estudios_musicales", "activo")
agregar_corista(3, "pepellido", "nombre", "correo", "cuerda", "experiencia", "lectura_musical", "estudios_musicales", "activo")
agregar_corista(4, "ape", "nombre", "correo", "cuerda", "experiencia", "lectura_musical", "estudios_musicales", "activo")
agregar_corista(5, "pepino", "nombre", "correo", "cuerda", "experiencia", "lectura_musical", "estudios_musicales", "activo")

agregar_corista(3, "apellido", "nombre", "correo", "cuerda", "experiencia", "lectura_musical", "estudios_musicales", "activo") # No es posible agregarlo, mismo código que el producto 3.
# Listamos todos los productos en pantalla
listar_coristas()
# Consultar un producto por su código
cod_cor = int(input("Ingrese el código del corista: "))
corista = consultar_corista(cod_cor)
if corista:
    print(f"Corista encontrado: {corista['codigo']} - {corista['apellido']}")
else:
    print(f'Corista {cod_prod} no encontrado.')
# Modificar un producto por su código
modificar_corista(1, "sape", "nombre", "correo", "cuerda", "experiencia", "lectura_musical", "estudios_musicales", "activo")
# Listamos todos los productos en pantalla
listar_coristas()
# Eliminamos un producto del inventario
eliminar_corista(5)
# Listamos todos los productos en pantalla
listar_coristas()
# ----------------------------------------------------------
