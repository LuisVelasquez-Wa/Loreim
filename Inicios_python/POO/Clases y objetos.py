        ### CON OBJETOS NO VIABLE ###

"""
Celular1_marca = "samsung"
celular2_marca = "apple"
celular3_marca = "huawei"

celular1_modelo = "S24"
celular2_modelo = "iPhone 13"
celular3_modelo = "Homor 8X"

celular1_camaraF = "48MP"
celular2_camaraF = "24MP"
celular3_camaraF = "12MP"

celular1_camaraT = "48MP"
celular2_camaraT = "48MP"
celular3_camaraT = "48MP"

print(celular2_camaraF)
"""


            ### CON OBJETOS VIABLE ###

class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estas haciendo un llamado desde un: {self.marca} {self.modelo}")
    
    def cortar(self):
        print(f"Cortaste la llamada desde tu: {self.modelo}")

celular1 = Celular("Apple", "13 PRO MAX", "24MP")
celular2 = Celular("Samsung","S24","12MP")


celular1.llamar()


