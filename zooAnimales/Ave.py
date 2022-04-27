from zooAnimales.animal import Animal

class Ave(Animal):
    _listado = []
    _halcones = 0
    _aguilas = 0
    def __init__(self, nombre, edad, habitat, genero, color):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = color
        Ave._listado.append(self)
    
    @staticmethod
    def movimiento():
        return "volarr"

    @classmethod
    def cantidadReptiles(cls):
        return len(cls._listado)

    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        halcon = Ave(nombre, edad, "montanas", genero, "cafe glorioso")
        cls._halcones += 1
        return halcon
        
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        aguila = Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
        cls._aguilas += 1
        return aguila

    def getListado(cls):
        return cls._listado  
    def setListado(self, listado):
        self._listado = listado

    def getColorPlumas(self):
        return self._colorPlumas
    def setColorEscamas(self, colorPlumas):
        self._colorPlumas = colorPlumas
