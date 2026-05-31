class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self._energia = 100

    def comer(self, cantidad):
        self._energia = min(100, self._energia + cantidad)
        return self

    def descansar(self):
        self._energia = 100
        return self

    def __str__(self):
        return f"{self.nombre} ({self.edad} anos) | energia: {self._energia}%"


class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def ladrar(self):
        return f"{self.nombre} dice: Guau guau!"

    def __str__(self):
        return f"{super().__str__()} | Raza: {self.raza}"


class Gato(Animal):
    def __init__(self, nombre, edad, es_domestico=True):
        super().__init__(nombre, edad)
        self.es_domestico = es_domestico

    def maullar(self):
        return f"{self.nombre} dice: Miau!"

    def __str__(self):
        tipo = "domestico" if self.es_domestico else "salvaje"
        return f"{super().__str__()} | Tipo: {tipo}"


class PerroGuia(Perro):
    def __init__(self, nombre, edad, raza, duenio):
        super().__init__(nombre, edad, raza)
        self.__duenio = duenio
        self.__horas_servicio = 0

    def trabajar(self, horas):
        self._energia = max(0, self._energia - horas * 10)
        self.__horas_servicio += horas
        return self

    @property
    def horas_totales(self):
        return self.__horas_servicio

    def __str__(self):
        return (f"{super().__str__()} | "
                f"Guia de: {self.__duenio} | "
                f"Horas servicio: {self.__horas_servicio}")


rex = PerroGuia("Rex", 4, "Labrador", "Carlos Vega")
rex.trabajar(3).comer(20)
print(rex)

print(isinstance(rex, PerroGuia))
print(isinstance(rex, Perro))
print(isinstance(rex, Animal))
print(isinstance(rex, Gato))

print(PerroGuia.__mro__)
