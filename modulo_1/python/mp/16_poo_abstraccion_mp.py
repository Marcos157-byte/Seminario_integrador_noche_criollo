from abc import ABC, abstractmethod


class MedioTransporte(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def velocidad_maxima(self) -> float:
        pass

    @abstractmethod
    def costo_por_km(self) -> float:
        pass

    def describir(self) -> str:
        return (f"{self.__class__.__name__} ({self.nombre}): "
                f"vel_max={self.velocidad_maxima()} km/h, "
                f"costo=${self.costo_por_km():.2f}/km")


class Avion(MedioTransporte):
    def velocidad_maxima(self) -> float:
        return 900.0

    def costo_por_km(self) -> float:
        return 0.45


class Tren(MedioTransporte):
    def velocidad_maxima(self) -> float:
        return 300.0

    def costo_por_km(self) -> float:
        return 0.12


class Autobus(MedioTransporte):
    def velocidad_maxima(self) -> float:
        return 110.0

    def costo_por_km(self) -> float:
        return 0.05


transportes = [Avion("Boeing 737"), Tren("AVE"), Autobus("Expreso Norte")]

for t in transportes:
    print(t.describir())

costo_total = sum(t.costo_por_km() * 500 for t in transportes)
print(f"Costo total para 500 km con todos los medios: ${costo_total:.2f}")
