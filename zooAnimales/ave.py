from .animal import Animal, setBase
from gestion.zona import Zona

class Ave(Animal):
    _listado = []
    _halcones = 0
    _aguilas = 0

    def __init__(self, colorPlumas: str) -> None:
        super().__init__()
        self._colorPlumas = colorPlumas

    def getColorPlumas(self) -> str:
        return self._colorPlumas

    def setColorPlumas(self, colorPlumas: str) -> None:
        self._colorPlumas = colorPlumas

    @classmethod
    def cantidadAves(cls) -> int:
        return len(cls._listado)

    def movimiento() -> str:
        return "volar"

    @classmethod
    def crearHalcon(cls, nombre: str, edad: int, genero: str):
        halcon = cls("cafe glorioso")
        setBase(halcon, nombre, edad, "montañas", genero)
        cls._listado.append(halcon)
        cls._halcones += 1
        return halcon

    @classmethod
    def crearAguila(cls, nombre: str, edad: int, genero: str):
        aguila = cls("blanco y amarillo")
        setBase(aguila, nombre, edad, "montañas", genero)
        cls._listado.append(aguila)
        cls._aguilas += 1
        return aguila

    @classmethod
    def cantidadHalcones(cls) -> int:
        return cls._halcones

    @classmethod
    def cantidadAguilas(cls) -> int:
        return cls._aguilas

