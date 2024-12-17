from .animal import Animal

class Reptil(Animal):

    _listado = list()
    _iguanas = 0
    _serpientes = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(self)

    @classmethod
    def cantidadReptiles(cls): return len(cls._listado)

    def movimiento(): return "reptar"

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        iguana = cls(nombre, edad, "humedal", genero, "verde", 3)
        cls._iguanas += 1
        return iguana
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        serpiente = cls(nombre, edad, "jungla", genero, "blanco", 1)
        cls._serpientes += 1
        return serpiente
    
    def getColorEscamas(self): return self._colorEscamas
    def setColorEscamas(self, escamas): self._colorEscamas = escamas

    def getLargoCola(self): return self._largoCola
    def setLargoCola(self, largoCola): self._largoCola = largoCola