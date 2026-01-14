class Animal():
    def sonido(self):
        pass

class Gato(Animal):
    def sonido (self):
        return "Miau mierda"
    
class Perro(Animal):
    def sonido (self):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro ()

hacer_sonido(gato)
print(perro.sonido())
hacer_sonido(perro)