from .animal import Animal

class Anfibio(Animal):

    _listado = list()
    _ranas = 0
    _salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    @classmethod
    def cantidadAnfibios(cls): return len(cls._listado)

    def movimiento(): return "saltar"

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = cls(nombre, edad, "selva", genero, "rojo", True)
        cls._ranas += 1
        return rana
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = cls(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls._salamandras += 1
        return salamandra
    
    def getColorPiel(self): return self._colorPiel
    def setColorPiel(self, color): self._colorPiel = color

    def getVenenoso(self): return self._venenoso
    def setVenenoso(self, venenoso): self._venenoso = venenoso