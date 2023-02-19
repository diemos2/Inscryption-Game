#Definición de la clase Carta
class Carta:
    def __init__(self, mazo, card_id):
        carta = mazo.get(card_id)       #Obtención del value de cada key del diccionario cartas disponibles
        #Definición de los atributos de acuerdo a la posición de cada value del diccionario cartas disponibles
        self.id = card_id
        self.nombre = carta[0]
        self.tipo = carta[1]
        self.ataque = carta[2]
        self.defensa = carta[3]
        self.sacrificio = carta[4]
        self.convocar = carta[5] # o quien haga sus veces
        self.cant = 1