from animal import setBase
from gestion.zona import Zona

class Pez:
    _listado = []
    _salmones = 0
    _bacalaos = 0

    def __init__(self, colorEscamas: str, cantidadAletas: int) -> None:
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas

    def getColorEscamas(self) -> str:
        return self._colorEscamas

    def setColorEscamas(self, colorEscamas: str) -> None:
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self) -> int:
        return self._cantidadAletas

    def setCantidadAletas(self, cantidadAletas: int) -> None:
        self._cantidadAletas = cantidadAletas

    @classmethod
    def cantidadPeces(cls) -> int:
        return len(cls._listado)

    @classmethod
    def crearSalmon(cls, nombre: str, edad: int, genero: str, zona: Zona):
        salmon = cls("rojo", 6)
        setBase(salmon, nombre, edad, "océano", genero, zona)
        cls._listado.append(salmon)
        cls._salmones += 1
        return salmon

    @classmethod
    def crearBacalao(cls, nombre: str, edad: int, genero: str, zona: Zona):
        bacalao = cls("gris", 6)
        setBase(bacalao, nombre, edad, "océano", genero, zona)
        cls._listado.append(bacalao)
        cls._bacalaos += 1
        return bacalao

    @classmethod
    def cantidadSalmones(cls) -> int:
        return cls._salmones

    @classmethod
    def cantidadBacalaos(cls) -> int:
        return cls._bacalaos