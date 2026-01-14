            ### CLASES ###

class MyEmptyPerson:
    pass 

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "sin alias"):
        self.full_name = f"{name} {surname} *****{alias}*****"
        self.__name = name # Propiedad privada.
    
    def walk(self):
        print(f"{self.full_name} esta caminando.")


my_person = Person("Luis", "Velasquez")
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Loreim", "Warrior", "La luz del alba")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Alanaya (la loca de la magia arcana)"
my_other_person.walk()
print(my_other_person.full_name)