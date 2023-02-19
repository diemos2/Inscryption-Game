from unicodedata import name

from carta import Carta
from mazo import Mazo


class Player:
    def __init__(self):
        self.name = "unknown"
        self.mazo = Mazo()
        self.sacrificio = {'S001': ['ELECTRO RECLUTAS REALES', 'SACRIFICIO' , 0, 1, 1, 0]}
        self.mazo.dictToCarta(self.sacrificio, "S001")
        self.mazo.cartas.get("S001").cant = 15

    def setName(self):
        self.name = input("Por favor ingrese el nombre: ")

    def getName(self):
        return self.name

    def convocar(self):
        pass