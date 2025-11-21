"""El método de fábrica
es un patrón de diseño creacional en Python que crea objetos sin especificar sus clases concretas. En lugar de llamar directamente al constructor, se utiliza un método de fábrica para crear objetos, lo que permite a las subclases decidir qué clase crear. Esto hace que el código sea más flexible, fácil de mantener y extensible
"""

from abc import ABC, abstractmethod


class Notificacion(ABC):
    """Creamso nuestra clase paadre para heredar un método abstracto y crear nuestra fabrica"""

    @abstractmethod
    def enviar(self, mensaje: str):
        pass


class Email(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando Email: {mensaje}")


class SMS(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviandoa Sms: {mensaje}")


class Facebook(Notificacion):
    def enviar(self, mensaje: str):
        print(f"Enviando por Facebook: {mensaje}")


# Creo mií fabrica
class NotificacionesFactory:
    @staticmethod
    def crear(tipo: str) -> Notificacion:
        if tipo == "email":
            return Email()
        elif tipo == "sms":
            return SMS()
        elif tipo == "facebook":
            return Facebook()
        else:
            raise ValueError("Tipo de notificación no soportada")


# Al intanciar nuestro objeto noti le pasamos como parametro a la calse el tipo de notificacion sea email, sms, otras
noti = NotificacionesFactory.crear("facebook")
noti.enviar("Hola mundo")
