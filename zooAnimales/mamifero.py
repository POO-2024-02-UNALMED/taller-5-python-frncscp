from animal import Animal, setBase
from gestion.zona import Zona

class Mamifero(Animal):
    _listado = []
    _leones = 0
    _caballos = 0

    def __init__(self, pelaje: bool, patas: int) -> None:
        super().__init__()
        self._pelaje = pelaje
        self._patas = patas

    def getPelaje(self) -> bool:
        return self._pelaje

    def setPelaje(self, pelaje: bool) -> None:
        self._pelaje = pelaje

    def getPatas(self) -> int:
        return self._patas

    def setPatas(self, patas: int) -> None:
        self._patas = patas

    @classmethod
    def cantidadMamiferos(cls) -> int:
        return len(cls._listado)

    def movimiento() -> str:
        return "caminar"

    @classmethod
    def crearLeon(cls, nombre: str, edad: int, habitat: str, genero: str, zona: Zona):
        leon = cls(True, 4)  
        setBase(leon, nombre, edad, "selva", genero, zona)
        cls._listado.append(leon)
        cls._leones += 1
        return leon

    @classmethod
    def crearCaballo(cls, nombre: str, edad: int, habitat: str, genero: str, zona: Zona):
        caballo = cls(True, 4)  
        setBase(caballo, nombre, edad, "pradera", genero, zona)
        cls._listado.append(caballo)
        cls._caballos += 1
        return caballo