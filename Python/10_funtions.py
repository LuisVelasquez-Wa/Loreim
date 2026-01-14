            ### FUNCTIONS ###

def my_function (): 
    print("Esto es una funcion")

my_function ()
my_function ()
my_function ()

def sum_two_values (firts_number, second_number):
    print(firts_number + second_number)

sum_two_values (5, 7)
sum_two_values (679, 7)
sum_two_values ("124", "7")

def sum_two_values_with_return (firts_value, second_value):
    return firts_value + second_value

my_result = sum_two_values_with_return (10,5)
print(my_result)

def print_name (name, surname):
    print (f"{name} {surname}")
print_name(surname = "Luis", name = "Velasquez")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print (f"{name} {surname} {alias}")
print_name_with_default("Luis", "Velasquez")

def print_texts (*texts):
    for text in texts:
        print(text.upper())
print_texts("Hola", "Python", "Loreim")
print_texts("Hola")