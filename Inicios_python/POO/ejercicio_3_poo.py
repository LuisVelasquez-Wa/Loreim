class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad
        self.fuerza = fuerza

    def __repr__(self):
        return f"{self.nombre}(Fuerza: {self.fuerza},Velocidad: {self.velocidad})"
    
    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + otro_pj.nombre
        nueva_fuerza = round(((self.fuerza + otro_pj.fuerza)/2)**1.5)
        nueva_velocidad = round(((self.velocidad + otro_pj.fuerza)/2)**1.5)
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

goku = Personaje("Goku", 100, 100)
vegeta = Personaje("Vegeta", 50, 50)
jiren = Personaje("Jiren", 150, 150)

gogeta = goku + vegeta
jiren = gogeta + jiren

print(jiren)