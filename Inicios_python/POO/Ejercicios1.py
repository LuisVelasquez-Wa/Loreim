class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print("Estudiando...")

nombre = input("Digame su nombre: ")
edad = input("Ahora digame su edad: ")
grado = input("Por ultimo, digame en que grado esta: ")

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE UNIVERSITARIO: \n\n
      Nombre: {estudiante.nombre}\n
      Edad: {estudiante.edad}\n
      Grado: {estudiante.grado}\n
""")
while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()