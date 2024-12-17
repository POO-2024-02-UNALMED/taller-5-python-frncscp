from .animal import Animal

class Mamifero(Animal):

    _listado = list()
    _caballos = 0
    _leones = 0

    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(self)

    @classmethod
    def cantidadMamiferos(cls): return len(cls._listado)

    @classmethod
    def crearCaballo(cls, nombre, edad, genero):
        caballo = cls(nombre, edad, "pradera", genero, True, 4)
        cls._caballos += 1
        return caballo
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero):
        leon = cls(nombre, edad, "selva", genero, True, 4)
        cls._leones += 1
        return leon
    
    def getPelaje(self): return self._pelaje
    def setPelaje(self, pelaje): self._pelaje = pelaje

    def getPatas(self): return self._patas
    def setPatas(self, patas): self._patas = patas