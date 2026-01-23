            ### SETS ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente nos indica diccionario.

my_other_set = {"Luis", "Velasquez", 30}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Loreim")

print(my_other_set) # Un set no es una estructura ordenada.

my_other_set.add("Loreim") # Un set no admite repetidos.

print(my_other_set)

print("Luis" in my_other_set)
print("Lorm" in my_other_set)

my_other_set.remove("Luis")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined,

my_set = {"Luis", "Velasquez", 30}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Warrior", "Mage", "Paladin"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union({"DK", "Chaman"}))

print(my_new_set.difference(my_set))