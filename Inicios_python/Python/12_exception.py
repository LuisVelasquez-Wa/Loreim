            ### EXCEPTION HANDLING ###

numberOne = 5
numberTwo = 1
numberTwo = "1"


try:
    print(numberOne + numberTwo)
    print("No se a producido un error")
except:
    print("Se a producido un error")
else: # Opcional
    # Se ejecuta si no se produce una excepcion.
    print("La ejecucion continua correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecucion continua")

# Captura de la informacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("No se a producido un error")
except ValueError as error:
    # Se ejecuta si no se produce una excepcion
    print(error)

try:
    print(numberOne + numberTwo)
    print("No se a producido un error")
except ValueError as error:
     print(error)
except Exception as exceptionerror:
    print(exceptionerror)
