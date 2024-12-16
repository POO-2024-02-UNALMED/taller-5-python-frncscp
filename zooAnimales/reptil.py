from animal import setBase
from gestion.zona import Zona

class Pez:
    _listado = []
    _iguanas = 0
    _serpientes = 0

    def __init__(self, colorEscamas: str, largoCola: int) -> None:
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    def getColorEscamas(self) -> str:
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas: str) -> None:
        self._colorEscamas = colorEscamas

    def getLargoCola(self) -> int:
        return self._largoCola

    def setLargoCola(self, largoCola: int) -> None:
        self._largoCola = largoCola

    @classmethod
    def cantidadReptiles(cls) -> int:
        return len(cls._listado)

    @classmethod
    def crearIguana(cls, nombre: str, edad: int, genero: str, zona: Zona):
        iguana = cls("verde", 3)
        setBase(iguana, nombre, edad, "humedal", genero, zona)
        cls._listado.append(iguana)
        cls._iguanas += 1
        return iguana

    @classmethod
    def crearSerpiente(cls, nombre: str, edad: int, genero: str, zona: Zona):
        serpiente = cls("blanco", 1)
        setBase(serpiente, nombre, edad, "jungla", genero, zona)
        cls._listado.append(serpiente)
        cls._serpientes += 1
        return serpiente

    @classmethod
    def cantidadSerpientes(cls) -> int:
        return cls._serpientes

    @classmethod
    def cantidadIguanas(cls) -> int:
        return cls._iguanas
    
    def movimiento() -> str:
        return "reptar"