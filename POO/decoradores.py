
def decorador(funcion):
    def funcion_modificada ():
        print("\tBienvenido estimado")
        funcion()
    return funcion_modificada

# def saludo():
#     print("Luis")

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
    print("Hola luis como estas")

saludo()