from pydoc import plain
from mazo import Mazo
from carta import Carta
from player import Player

class Tablero:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

    def repartirCarta(self, mazo_origen):
        mazo_origen.cartas.pop("S001")
        tipo_carta = ["BASICA", "MEDIA", "SUPER"]
        for i in range(3):
            mazo_tipo = Mazo()
            mazo_tipo.cartas = mazo_origen.getCardsType(tipo_carta[i])
            contador = 2 #len(mazo_tipo)
            while contador > 0:
                if contador % 2 == 0:
                    mazo_tipo.printCartas()
                    print("{} por favor seleccione el ID de su carta".format(self.player1.getName())) #Imprimir cartas disponibles
                    id = input("") #Para tener en cuneta, validar ID de carta por si no existe
                    self.player1.mazo.recibirCarta(mazo_tipo, id)
                    contador -= 1
                else:
                    mazo_tipo.printCartas()
                    print("{} por favor seleccione el ID de su carta".format(self.player2.getName())) #Imprimir cartas disponibles
                    id = input("") #Para tener en cuneta, validar ID de carta por si no existe
                    self.player2.mazo.recibirCarta(mazo_tipo, id)
                    contador -= 1
                                    