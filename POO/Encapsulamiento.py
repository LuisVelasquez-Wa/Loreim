
""""
class MiClase:
    def __init__(self):
        self._atributo_privado = "Atributo privado."
    
    def _hablar_(self):
        print("Hola como estas.")

objeto = MiClase()
print(objeto._atributo_privado)
"""

class Persona:
    def __init__(self, nombre, edad):
        self._nombre =  nombre
        self._edad = edad
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre


dato = Persona("Luis", 30)

nombre = dato.get_nombre()
print(nombre)

dato.set_nombre ("Juan")
 
nombre = dato.get_nombre()
print(nombre)
