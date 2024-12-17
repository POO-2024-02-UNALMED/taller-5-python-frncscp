from .animal import Animal

class Pez(Animal):

    _listado = list()
    _bacalaos = 0
    _salmones = 0

    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez._listado.append(self)

    @classmethod
    def cantidadPeces(cls): return len(cls._listado)

    def movimiento(): return "nadar"

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        bacalao = cls(nombre, edad, "oceano", genero, "gris", 6)
        cls._bacalaos += 1
        return bacalao
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        salmon = cls(nombre, edad, "oceano", genero, "rojo", 6)
        cls._salmones += 1
        return salmon
    
    def getColorEscamas(self): return self._colorEscamas
    def setColorEscamas(self, escamas): self._colorEscamas = escamas

    def getCantidadAletas(self): return self._cantidadAletas
    def setCantidadAletas(self, aletas): self._cantidadAletas = aletas