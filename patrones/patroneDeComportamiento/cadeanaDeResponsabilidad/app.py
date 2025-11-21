"""El patrón
Cadena de Responsabilidad en Python es un patrón de diseño de comportamiento que permite pasar una solicitud a través de una cadena de manejadores. Cada manejador decide si procesa la solicitud o la pasa al siguiente en la cadena, permitiendo desacoplar al remitente de la solicitud de sus receptores. Es una forma de reemplazar las declaraciones if... elif... else anidadas con un diseño más flexible y dinámico
"""

from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, next_handler=None):
        self._next = next_handler

    @abstractmethod
    def process_reques(self, request):
        pass

    def handle(self, request):
        handled = self.process_reques(request)
        if not handled and self._next:
            return self._next.handle(request)


class AuthHandler(Handler):
    def process_reques(self, request):
        if request.get("user") == "Juan" and request.get("password") == "12345":
            print("Usuario autentificado")
            return False
        print("[ERROR]")
        return True


class RoleHandler(Handler):
    def process_reques(self, request):
        if request.get("role") == "admin":
            print("Usuario autentificado confirmado")
            return False
        print("[ERROR]")
        return True


chain = AuthHandler(RoleHandler())

request1 = {"user": "Juan", "password": "12345", "role": "admin"}
chain.handle(request1)
request2 = {"user": "Juan", "password": "12345", "role": "user"}
chain.handle(request2)
