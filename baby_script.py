#Llamado de las clases Mazo y Carta al programa principal las cuales se encuentran en sus respectivos códigos
from mazo import Mazo
from carta import Carta
from player import Player
from tablero import Tablero

#Definición del diccionario con todas las cartas disponibles para el juego
cartas_DISP = {'S001': ['ELECTRO RECLUTAS REALES', 'SACRIFICIO' , 0, 1, 1, 0], 'A001': ['ESQUELETOS', 'BASICA' , 1, 2, 2, 1], 'A002': ['TRIO DE MOSQUETEROS', 'BASICA' , 2, 1, 2, 1], 'A003': ['GÓLEM', 'BASICA' , 1, 1, 3, 1], 'A004': ['SABUESO DE LAVA', 'BASICA' , 2, 2, 1, 1], 'A005': ['DRAGON DE TIERRA', 'BASICA' , 0, 4, 1, 1], 'A006': ['JUGADOR DEL MIEDO', 'MEDIA' , 2, 3, 2, 3], 'A007': ['GIGANTE NOBLE', 'MEDIA' , 3, 2, 2, 3], 'A008': ['ENANO DIABOLICO', 'MEDIA' , 4, 1, 2, 3], 'A009': ['THUNDERBIRD', 'MEDIA' , 2, 1, 4, 3], 'A010': ['MAGO ARCANO', 'MEDIA' , 1, 5, 1, 3], 'A011': ['DEMONIO DE LA MALDAD ', 'SUPER' , 3, 5, 1, 5], 'A012': ['ANGEL DE LA CARIDAD', 'SUPER' , 5, 2, 2, 5], 'A013': ['SAN MANDARINA', 'SUPER' , 4, 4, 1, 5], 'A014': ['EL MARRANO VOLADOR', 'SUPER' , 3, 5, 1, 5], 'A015': ['QUEEN OF THE UNIVERSE', 'SUPER' , 9, 2, 0, 7], 'B001': ['ROBOT DE SERVICIO', 'BASICA' , 1, 2, 2, 1], 'B002': ['LAGARTO MECANICO', 'BASICA' , 3, 1, 1, 1], 'B003': ['LANZALLAMAS ELECTRONICO', 'BASICA' , 2, 1, 2, 1], 'B004': ['T-5000', 'BASICA' , 3, 1, 1, 1], 'B005': ['MOTO-KILLER', 'BASICA' , 2, 2, 1, 1], 'B006': ['MURDER ELETRO PUMP', 'MEDIA' , 2, 4, 1, 3], 'B007': ['METAL KNIGTH', 'MEDIA' , 2, 2, 3, 3], 'B008': ['WARRIOR OF THE INTERNET', 'MEDIA' , 2, 3, 2, 3], 'B009': ['LAGARTO ELÉCTRICO', 'MEDIA' , 1, 2, 4, 3], 'B010': ['MECANIC DRON', 'MEDIA' , 5, 1, 1, 3], 'B011': ['LAZER MORTAL', 'SUPER' , 2, 4, 3, 5], 'B012': ['MOTHER BOARD FROM HELL', 'SUPER' , 4, 5, 0, 5], 'B013': ['COMPUTER FROM HEAVEN', 'SUPER' , 2, 3, 4, 5], 'B014': ['VAPORWAVE DJ', 'SUPER' , 3, 4, 2, 5], 'B015': ['BENDER', 'SUPER' , 2, 9, 0, 7]}

#Creación de cartas disponibles como objeto de clase Mazo
cartas_disponibles = Mazo()
#Llamado del método diccToCartas de la clase Mazo el cual crea a través del método dictToCarta un diccionario de objetos tipo Carta con las cartas disponibles para el juego 
cartas_disponibles.diccToCartas(cartas_DISP)
#Llamado del método printCarta de la clase Mazo el cual imprime toda la información necesaria para la carta seleccionada
#cartas_disponibles.printCarta("A015")

# Funcion inicio de turno
def turnInit():
    end_turn = False
    while end_turn == False:
        print("Por favor seleccione acción:")
        print("""
        1. Convocar
        2. Sacrificar
        3. Atacar!
        """)
        command = input("-->")
        print("")
        if command == "1":
            print("Convocando...\n")
        if command == "2":
            print("Sacrificando...\n")
        if command == "3":
            print("Atacando...")
            print("Fin del turno.\n")
            end_turn = True

#basicas = cartas_disponibles.getCardsType("BASICA")
#print (getCardType(cartas_DISP, "MEDIA"))
#print (getCardType(cartas_DISP, "SUPER"))


#     basicas = (getCardType(cartas_DISP, "BASICA"))
#     #print (basicas)
#     mazo_jugador_1 = Mazo()
#     for i in range(3):
#         print (basicas)
#         comando = input("Seleccione su carta ID: ")
#         mazo_jugador_1.recibirCarta(basicas, comando)
#     "mazo_jugador_1.printMazo()"
#     "print(mazo_jugador_1.cartas[i].nombre for i in range (3))"
#     for i in range(3):
#         print("carta 1-nombre: {}, ID: {}".format(mazo_jugador_1.cartas[i].nombre, mazo_jugador_1.cartas[i].ID))
#     #print(carta.nombre, "\n", carta.ataque, "\n", carta.defensa, "\n", carta.ID)

def main():
    print("Bienvenido a mi jueguito uwu")

    # Iniciar Tablero
    tablero = Tablero()

    # Se configuran jugadores
    print("Jugador 1")
    tablero.player1.setName()
    print("Jugador 2")
    tablero.player2.setName()

    # Se reparten cartas
    tablero.repartirCarta(cartas_disponibles)
    tablero.player1.mazo.printCartas()
    print("---------------------------------------------------------\n")
    tablero.player2.mazo.printCartas()

    # Jugador empieza turno
    print("Jugador 1 empieza... \n")
    turnInit()

if __name__ == "__main__":
    main()

