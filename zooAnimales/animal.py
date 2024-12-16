import sys
sys.path.append('/home/franc/code/oop/python/taller-5-python-frncscp/')
from gestion.zona import Zona

class Animal:

    _totalAnimales = 0

    def __init__(self, nombre: str = None, edad: int = None, habitat: str = None, genero: str = None, zona = None) -> None:
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

    def movimiento() -> str:
        return "desplazarse"
    
    def totalPorTipo() -> str:
        pass

    def __str__(self) -> str:
        base = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi género es {self._genero}"
        if type(self._zona) is Zona:
            dlc = f", la zona en la que me ubico es {self._zona.getNombre()}, en el {self._zona.getZoo().getNombre()}"
            return base + dlc
        else:
            return base + "."
        
    def getNombre(self) -> str:
        return self._nombre
    def setNombre(self, nombre: str) -> None:
        self._nombre = nombre

    def getEdad(self) -> int:
        return self._edad
    def setEdad(self, edad: int) -> None:
        self._edad = edad

    def getHabitat(self) -> str:
        return self._habitat
    def setHabitat(self, habitat: str) -> None:
        self._habitat = habitat

    def getGenero(self) -> str:
        return self._genero
    def setGenero(self, genero: str) -> None:
        self._genero = genero

    def getZona(self):
        return self._zona
    def setZona(self, zona) -> None:
        self._zona = zona

    def getTotalAnimales(cls) -> int:
        return cls._totalAnimales
    
def setBase(obj: Animal, nombre: str, edad: int, habitat: str, genero: str, zona):
    obj.setNombre(nombre)
    obj.setEdad(edad)
    obj.setHabitat(habitat)
    obj.setGenero(genero)
    obj.setZona(zona)