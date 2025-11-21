"""El "método adapter" en Python
es un patrón de diseño estructural que permite que objetos con interfaces incompatibles colaboren entre sí. Actúa como un puente o traductor entre dos objetos, envolviendo a uno para que sus métodos se ajusten a la interfaz que el otro espera. Esto se logra creando una clase adaptadora que, al recibir una llamada, traduce los parámetros y delega la acción a los métodos del objeto que envuelve
"""

# Usamos un clase que ya existe


class PagoDolar:
    def pagar(self, monto: float):
        print(f"Procesando paso en 💵 {monto:,.2f} USB")


# Clase incompatible(Tercera o servicio externo)
class PagoEuro:
    def pagos_en_euros(self, monto: float):
        print(f"Procesando pago en 💶 {monto:,.2f} EUR")


# Usaremos un adapdatador
class AdapterPagosEuro(PagoDolar):
    def __init__(
        self, pago_euro: PagoEuro, tasa_cambio: float = 0.9
    ):  # Creamos un parametro para los pagos en EUR, que reciba la clase PagoEuro()
        super().__init__()
        self.pago_euro = pago_euro
        self.tasa_cambio = tasa_cambio

    # Creamos un método para validar la converción del pago
    def pagar(self, monto: float):
        monto_euro = monto * self.tasa_cambio
        print(f"Convietiendo 💵 {monto:,.2f} USD ---> 💶 {monto_euro:,.2f} EUR")
        self.pago_euro.pagos_en_euros(monto_euro)


# creamso una función fuera de la clase para que procese el pago
def procesar_pago(pasarela, monto):
    pasarela.pagar(monto)


pago_usd = PagoDolar()
procesar_pago(pago_usd, 100)

# instanciamos la adaptacion dle pago en euros
pago_eur = AdapterPagosEuro(PagoEuro())
procesar_pago(pago_eur, 100)
