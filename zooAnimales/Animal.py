from gestion.zona import Zona
from gestion.zoologico import Zoologico

class Animal:
    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1

    def totalPorTipo(cls):
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        from zooAnimales.anfibio import Anfibio       

        return ("Mamiferos : "+str(len(Mamifero.getListado()))+"\n"
        +"Aves : "+str(len(Ave.getListado()))+"\n"
        +"Reptiles : "+str(len(Reptil.getListado()))+"\n"
        +"Peces : "+str(len(Pez.getListado()))+"\n"
        +"Anfibios : "+str(len(Anfibio.getListado()))+"\n")

    def toString(self):
        if self._zona is None:
            return "Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}".format(self._nombre, self._edad, self._habitat,self._genero)
        else:
            return "Mi nombre es {}, tengo una edad de {}, habito en {} y mi genero es {}, la zona en la que me ubico es {}, en el {}".format(self._nombre, self._edad, self._habitat, self._genero, self._zona.getNombre(), self._zona._zoo.getNombre())
    
    @staticmethod
    def movimiento(cls):
        return "desplazarse"
    
    
    def getNombre(self):
        return self._nombre
    def setNombre(self, nombre):
        self._nombre = nombre


    def getEdad(self):
        return self._edad
    def setEdad(self, edad):
        self._edad = edad
    
    @classmethod
    def getTotalAnimales(clc):
        return clc._totalAnimales
    @classmethod
    def setTotalAnimales(clc, totalAnimales):
        clc._totalAnimales = totalAnimales

    def getHabitat(self):
        return self._habitat
    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero
    def setGenero(self,genero):
        self._genero = genero
    
    def getZona(self):
        return self._zona
    def setZona(self, zona):
        self._zona = zona
    