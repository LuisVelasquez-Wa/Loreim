            ### STRINGS ###
my_String = 'Mi string'
my_other_string = 'Mi otro string'

print(len(my_other_string))
print(len(my_String))

print(my_other_string + " " + my_String)

my_new_line_string = "Este es un salto de linea \ncon salto de linea"
print(my_new_line_string)

my_tap_string = "\tEste es un string con tabulacion"
print(my_tap_string)

my_scape_string = "\tEste estring \ntiene un escapado"
print(my_scape_string)

# FORMATEO
name, surname, age = "Luis", "Velasquesz", 30
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))

print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# DESEMPAQUETADO DE CARACTERTES

lenguage = "PYTHON"
a, b, c, d, e, f = lenguage
print(a)
print(e)

# DIVISION
lenguage_slice = lenguage[1:3]
print(lenguage_slice)

lenguage_slice = lenguage[-2]
print(lenguage_slice)

# REVERSO

reversed_lenguage = lenguage [::-1]
print(reversed_lenguage)

# FUNCIONES

print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count("t"))
print(lenguage.isnumeric())
print("1".isnumeric())
print(lenguage.lower())
print(lenguage.lower().isupper())

