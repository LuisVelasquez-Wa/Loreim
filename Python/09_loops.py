            ### LOOPS ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break

    print(my_condition)

print("La ejecucion continua")

# For

my_list = [20, 23, 21, 25, 435, 2, 4525,24]

for element in my_list:
    print(element)
else:
    print("El bucle for para list a finalizado")

my_tuple = (30, 1.65, "Luis", "Velasquez")

for element in my_tuple:
    print(element)
else:
    print("El bucle for para tuple a finalizado")

my_set = {"Luis", "Velasquez", 30}

for element in my_set:
    print(element)
else:
    print("El bucle for para set a finalizado")

my_other_dict = {"Nombre": "Luis", "Apellido": "Velasquez", "Edad": 30, 1:"Python"}

for element in my_other_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionario a finalizado")
