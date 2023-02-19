#Llamado de la clase Carta al script Mazo
from carta import Carta

#Definición de la clase Mazo
class Mazo:
    def __init__(self):
        self.cartas = {}    #Creación del atributo cartas el cual será un diccionario de objetos de clase Carta

    #El método recibircarta retira las cartas que ha elegido cada jugador de las cartas disponibles 
    def recibirCarta (self, mazo_origen, id):
        carta = mazo_origen.cartas.get(id)
        self.cartas[id] = carta
        mazo_origen.cartas.pop(id)

    #El método printCarta imprime toda la información necesaria para la carta seleccionada en la terminal
    def printCarta(self, id): #para arreglar = imprimir los objetos
        print("==========================")#26 =
        print('|        [ {} ]        |'.format(self.cartas.get(id).id))
        print('| {:23}{}'.format(self.cartas.get(id).nombre, "|"))
        print('|    {:12} {:3d}    {}'.format("ATAQUE:", self.cartas.get(id).ataque, "|"))
        print('|    {:12} {:3d}    {}'.format("DEFENSA:", self.cartas.get(id).defensa, "|"))
        print('|    {:12} {:3d}    {}'.format("SACRIFICIO:", self.cartas.get(id).sacrificio, "|"))
        print('|    {:12} {:3d}    {}'.format("CONVOCAR:", self.cartas.get(id).convocar, "|"))
        print("==========================")#2& =

    #El método printCartas imprime todas las cartas de acuerdo a lo definido en printCarta
    def printCartas (self):
        for key in self.cartas:
            self.printCarta(key)
            print ("")

    #El método getCardsType clasifica las cartas de acuerdo al tipo al que pertencen a fin de que sea equitativo la elección por parte de los jugadores
    def getCardsType (self, tipo_carta): #(cartas_DISP, 'super')
        out_cards_for_type = {}     #Creación del atributo out_cards_for_type el cual será un diccionario de objetos de clase Carta
        for carta_key in self.cartas:
            tipo = self.cartas.get(carta_key).tipo
            if tipo == tipo_carta:
                out_cards_for_type[carta_key] = self.cartas.get(carta_key)
            else:
                continue
        return out_cards_for_type
    
    #El método dictToCarta crea un objeto de clase Carta con base a una carta disponible
    def dictToCarta (self, carta_dicc, id):
        carta = Carta(carta_dicc, id)
        self.cartas[id] = carta

    #El método diccToCartas crea a través del método dictToCarta un diccionario de objetos tipo Carta con las cartas disponibles para el juego
    def diccToCartas (self, cartas_dicc):
        for key in cartas_dicc:
            self.dictToCarta(cartas_dicc, key)