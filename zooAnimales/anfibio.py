from .animal import Animal, setBase
from gestion.zona import Zona

class Anfibio(Animal):
    _listado = []
    _ranas = 0
    _salamandras = 0

    def __init__(self, colorPiel: str, venenoso: bool) -> None:
        super().__init__()
        self._colorPiel = colorPiel
        self._venenoso = venenoso

    @classmethod
    def cantidadAnfibios(cls) -> int:
        return len(cls._listado)
    
    def movimiento() -> str:
        return "saltar"
    
    @classmethod
    def crearRana(cls, nombre: str, edad: int, genero: str):
        rana = cls("rojo", True)
        setBase(rana, nombre, edad, "selva", genero)
        cls._ranas += 1
        cls._listado.append(rana)
        return rana

    @classmethod
    def crearSalamandra(cls, nombre: str, edad: int, genero: str):
        salamandra = cls("negro y amarillo", False)
        setBase(salamandra, nombre, edad, "selva", genero)
        cls._salamandras += 1
        cls._listado.append(salamandra)
        return salamandra