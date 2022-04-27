from zooAnimales.animal import Animal

class Anfibio(Animal):
    _listado = []
    _ranas = 0
    _salamandras = 0
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._venenoso = venenoso
        self._colorPiel = colorPiel       
        Anfibio._listado.append(self)

    @staticmethod
    def movimiento():
        return "saltar"

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        rana = Anfibio(nombre, edad, "selva", genero, "rojo", True)
        cls._ranas += 1
        return rana
        
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        salamandra = Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls._salamandras += 1
        return salamandra

    def getListado(cls):
        return cls._listado  
    def setListado(self, listado):
        self._listado = listado

    def isVenenoso(self):
        return self._venenoso
    def setColorEscamas(self, venenoso):
        self._venenoso = venenoso

    def getColorPiel(self):
        return self._colorPiel
    def setCantidadAletas(self, colorPiel):
        self._colorPiel = colorPiel
