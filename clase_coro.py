# Definición de la clase "coro" en la cual se agregaran coristas de la base de datos como miembros???
class Coro:
    coristas = []
    
    def agregar_corista(self, codigo, apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo):
        if self.consultar_corista(codigo):
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
        
        self.coristas.append(nuevo_corista)
        return True

    def consultar_corista(self, codigo):
        for corista in self.coristas:
            if corista['codigo'] == codigo:
                return corista
        return False

    def modificar_corista(self, apellido, nombre, correo, cuerda, experiencia, lectura_musical, estudios_musicales, activo):
        for corista in self.coristas:
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

    def listar_coristas(self):
        print("-" * 50)
        for corista in self.coristas:
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
            
    def eliminar_corista(self, codigo):
        for corista in self.coristas:
            if corista['codigo'] == codigo:
                self.coristas.remove(corista)
                return True
        return False

    def mostrar_corista(self, codigo):
        corista = self.consultar_corista(codigo)
        if corista:
            print("-" * 50)
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
        else:
            print("Corista no encontrado.")
        
# PRUEBAS --------------------------
coro = Coro()
coro.agregar_corista(1, "pepellido", "nombre", "correo", "cuerda", "experiencia", "lectura_musical", "estudios_musicales", "activo")
coro.agregar_corista(2, "pepito", "nombre", "correo", "cuerda", "experiencia", "lectura_musical", "estudios_musicales", "activo")
print("Listado de coristas:")
coro.listar_coristas()
print()
print("Datos de un corista:")
coro.mostrar_corista(1)
coro.eliminar_corista(1)
print()
print("Listado de coristas:")
coro.listar_coristas()
#-----------------------------------


