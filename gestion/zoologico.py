class Zoologico:
    #_nombre = None
    #_ubicacion = None
    #_zonas = None

    def __init__(self, nombre: str, ubic: str, zonas: list) -> None:
        self._nombre = nombre
        self._ubicacion = ubic
        self.zonas = zonas
    
    def agregarZonas(self, zona: list) -> None:
        self._zonas.append(zona)

    def cantidadTotalAnimales(self) -> int:
        return sum([zona.cantidadAnimales() for zona in self._zonas])
    
    def getNombre(self) -> str:
        return self._nombre
    def setNombre(self, nombre: str) -> None:
        self._nombre = nombre

    def getUbicacion(self) -> str:
        return self._ubicacion
    def setUbicacion(self, ubic: str) -> None:
        self._ubicacion = ubic

    def getZonas(self) -> list:
        return self._zonas
    def setZonas(self, zonas: list) -> None:
        self._zonas = zonas 