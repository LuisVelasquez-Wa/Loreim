            ### OPERADORES ###
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)

print("string de prueba" + " segundo string de prueba")
print("string de prueba " + str( 5))
print("string de prueba " * 5)
print("string de prueba " * (2 ** 3))

my_float = 2.5 * 2
print("string de prueba" * int(my_float))

# OPERADORES COMPARATIVOS

'''
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
'''

print("hola" > "python")
print("hola" < "python")
print("hola" >= "zola") # ORDEN ALFABETICO POR ASCII
print(len("hola") >= len("zola")) # CUENTA DE CARACTERES
print("hola" <= "python")
print("hola" == "hola")
print("hola" != "python")

# OPERADORES LOGICOS

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(not(3>4))