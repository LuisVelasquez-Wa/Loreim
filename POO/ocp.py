class Notificador:
    def __init__(self,usuario,mensaje):
        self.usario = usuario
        self.mensaje = mensaje
    def notificar(self):
        raise NotImplemented
    
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"Enviando mensaje a {self.usuario.email}")

class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"Enviando un sms a {self.usario.sms}")





















