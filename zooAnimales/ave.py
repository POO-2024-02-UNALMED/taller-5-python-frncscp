from .animal import Animal

class Ave(Animal):

    _listado = list()
    _aguilas = 0
    _halcones = 0

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave._listado.append(self)

    @classmethod
    def cantidadAves(cls): return len(cls._listado)

    def movimiento(): return "volar"

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = cls(nombre, edad, "montanas", genero, "cafe glorioso")
        cls._halcones += 1
        return halcon
    
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = cls(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls._aguilas += 1
        return aguila
    
    def getColorPlumas(self): return self._colorPlumas
    def setColorPlumas(self, color): self._colorPlumas = color