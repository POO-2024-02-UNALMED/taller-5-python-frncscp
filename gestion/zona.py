from gestion.zoologico import Zoologico
#from zooAnimales.animal import Animal

class Zona:
    #_nombre = None
    #_zoo = None
    #_animales = None

    def __init__(self, nombre: str):#, zoo: Zoologico, animales: list) -> None:
        self._nombre = nombre
        self._zoo = None
        self._animales = list()

    def agregarAnimales(self, animal) -> None:
        self._animales.append(animal)
    def cantidadAnimales(self) -> int:
        return len(self._animales)
    
    def getNombre(self) -> str:
        return self._nombre
    def setNombre(self, nombre: str) -> None:
        self._nombre = nombre

    def getZoo(self) -> Zoologico:
        return self._zoo
    def setZoo(self, zoo: Zoologico) -> None:
        self._zoo = zoo

    def getAnimales(self) -> list:
        return self._animales
    def setAnimales(self, animales: list) -> None:
        self._animales = animales 