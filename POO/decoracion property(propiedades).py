class Persona:
    def __init__(self, nombre, edad):
        self.__nombre =  nombre
        self._edad = edad
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre



dato = Persona("Luis", 30)

nombre = dato.nombre
print(nombre)


dato.nombre = "Juan"

nombre = dato.nombre
print(nombre)

del dato
print('loco')