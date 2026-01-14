class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.naciolaidad = nacionalidad

    def hablar(self):
        print("Hola, estoy hablando un poco")

class Artista: 
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad} ")

class EmpleadoArtista (Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarte(self):
        print(f"Hola soy {self.nombre} y mi habilidad es {self.habilidad} deseo un salario de {self.salario} en una empresa de {self.empresa}.")
    
luis = EmpleadoArtista("Luis", 30, "peruano", "Hueviar", 3000, "Tecnologia")

luis.presentarte()

herencia = issubclass(EmpleadoArtista, Artista)
isinstance = isinstance(luis, EmpleadoArtista)
print(isinstance)