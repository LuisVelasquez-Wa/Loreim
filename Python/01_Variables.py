            ### VARIABLES ###
my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to__str_variable = str(my_int_variable)
print(my_int_to__str_variable)
print(type(my_int_to__str_variable))

my_bool_variable = False
print(my_bool_variable)

#CONCATENACION DE VARIABLES EN UN PRINT
print("Este es el valor de:", my_bool_variable)

# FUNCIONES DE SISMTEA
print(len(my_string_variable))

# VARIABLES DE UNA SOLA LINEA
name, surname, alias, age = "Luis","Velasquez","Ingeniero", 30
print("Me llamo:", name, surname, ".Mi alias es:", alias, ".Mi edad es:", age)

# INPUTS
'''
name = input("Cual es tu nombre?")
age = input("Y tu edad?")
print(name)
print(age)
'''

# CAMBIAMOS SU TIPO
name = 30
age = "Luis"
print(name)
print(age)

# FORZAMOS EL TIPO
adress: str = 'Mi direccion'
adress = 30
adress = True
adress = 9.2
print(type(adress))