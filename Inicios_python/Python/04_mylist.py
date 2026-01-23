            ### LISTS ###
my_list = list()
my_other_list = []
print(len(my_list))

my_list = [20, 23, 21, 25, 435, 2, 4525,24]
print(my_list)
print(len(my_list))

my_other_list = [30, 1.65, "Luis", "Velasquez"]
print(type(my_other_list)) 
print(type(my_list))

print(my_other_list[0]) 
print(my_other_list[3]) 
print(my_list.count(24))
#print(my_other_list[4]) index eror porque esta fuera del rango.

age, height, name, surname = my_other_list
print(name)

name, height, surname, age = my_other_list[2], my_other_list[2], my_other_list[3], my_other_list[1]
print(age)

my_other_list.append("Loreim")
print(my_other_list)

my_other_list.insert(4, "Rojo")
print(my_other_list)

my_other_list [4]= "Verde"
print(my_other_list)

my_other_list.remove( "Verde")
print(my_other_list)

my_list.remove(435)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(3)
print(my_pop_element)
print(my_list)

del my_list[3]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[:5])
