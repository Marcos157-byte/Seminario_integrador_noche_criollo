class MetodoPago:
    def __init__(self, titular, monto):
        self.titular = titular
        self.monto = monto

    def procesar(self):
        raise NotImplementedError("Las subclases deben implementar procesar()")

    def __str__(self):
        return f"{self.__class__.__name__} -> {self.titular}"


class PagoTarjeta(MetodoPago):
    def __init__(self, titular, monto, ultimos_digitos):
        super().__init__(titular, monto)
        self.ultimos_digitos = ultimos_digitos

    def procesar(self):
        return f"Tarjeta *{self.ultimos_digitos}: cobro de ${self.monto:.2f} a {self.titular}"


class PagoTransferencia(MetodoPago):
    def __init__(self, titular, monto, cuenta_destino):
        super().__init__(titular, monto)
        self.cuenta_destino = cuenta_destino

    def procesar(self):
        return f"Transferencia a cuenta {self.cuenta_destino}: ${self.monto:.2f} de {self.titular}"


class PagoEfectivo(MetodoPago):
    def procesar(self):
        return f"Pago en efectivo: ${self.monto:.2f} recibido de {self.titular}"


class PagoQR(MetodoPago):
    def __init__(self, titular, monto, codigo):
        super().__init__(titular, monto)
        self.codigo = codigo

    def procesar(self):
        return f"QR [{self.codigo}]: ${self.monto:.2f} pagado por {self.titular}"


def ejecutar_pagos(pagos: list):
    for pago in pagos:
        print(f"  {pago.procesar()}")


cobros = [
    PagoTarjeta("Ana Torres", 250.00, "4321"),
    PagoTransferencia("Luis Gomez", 780.50, "ES76-0049-1234"),
    PagoEfectivo("Maria Ruiz", 45.00),
    PagoQR("Carlos Vera", 120.00, "QR-2025-001"),
]

print("Procesando pagos:")
ejecutar_pagos(cobros)


# DUCK TYPING - sin herencia comun
class ExportadorCSV:
    def exportar(self, datos): print(f"Guardando en CSV: {str(datos)[:40]}...")

class ExportadorJSON:
    def exportar(self, datos): print(f"Guardando en JSON: {str(datos)[:40]}...")

class ExportadorPDF:
    def exportar(self, datos): print(f"Generando PDF: {str(datos)[:40]}...")


def generar_reporte(exportador, datos):
    exportador.exportar(datos)


reporte = {"ventas": 5000, "clientes": 120, "mes": "mayo"}
for exp in [ExportadorCSV(), ExportadorJSON(), ExportadorPDF()]:
    generar_reporte(exp, reporte)
