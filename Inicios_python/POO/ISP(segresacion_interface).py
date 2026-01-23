from abc import ABC, abstractclassmethod

class Comedor(ABC):

    @abstractclassmethod
    def comer(self):
        pass

class Trabajador(ABC):
    @abstractclassmethod
    def trabajar(self):
        pass

class Durmiente(ABC):
    @abstractclassmethod
    def dormir(self):
        pass

class Humano(Trabajador, Durmiente, Comedor):
    
    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")

class Robot(Trabajador):

    def trabajar(self):
        print("El Robot esta trabajando")


robot= Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()