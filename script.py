
from msilib.schema import Class

cartas_DISP = {'S001': ['ELECTRO RECLUTAS REALES', 15, 0, 1, 1, 0], 'A001': ['ESQUELETOS', 1, 1, 2, 2, 1], 'A002': ['TRIO DE MOSQUETEROS', 2, 2, 1, 2, 1], 'A003': ['GÓLEM', 3, 1, 1, 3, 1], 'A004': ['SABUESO DE LAVA', 4, 2, 2, 1, 1], 'A005': ['DRAGON DE TIERRA', 5, 0, 4, 1, 1], 'A006': ['JUGADOR DEL MIEDO', 1, 2, 3, 2, 3], 'A007': ['GIGANTE NOBLE', 2, 3, 2, 2, 3], 'A008': ['ENANO DIABOLICO', 3, 4, 1, 2, 3], 'A009': ['THUNDERBIRD', 4, 2, 1, 4, 3], 'A010': ['MAGO ARCANO', 5, 1, 5, 1, 3], 'A011': ['DEMONIO DE LA MALDAD ', 1, 3, 5, 1, 5], 'A012': ['ANGEL DE LA CARIDAD', 2, 5, 2, 2, 5], 'A013': ['SAN MANDARINA', 3, 4, 4, 1, 5], 'A014': ['EL MARRANO VOLADOR', 4, 3, 5, 1, 5], 'A015': ['QUEEN OF THE UNIVERSE', 5, 9, 2, 0, 7], 'B001': ['ROBOT DE SERVICIO', 1, 1, 2, 2, 1], 'B002': ['LAGARTO MECANICO', 2, 3, 1, 1, 1], 'B003': ['LANZALLAMAS ELECTRONICO', 3, 2, 1, 2, 1], 'B004': ['T-5000', 4, 3, 1, 1, 1], 'B005': ['MOTO-KILLER', 5, 2, 2, 1, 1], 'B006': ['MURDER ELETRO PUMP', 1, 2, 4, 1, 3], 'B007': ['METAL KNIGTH', 2, 2, 2, 3, 3], 'B008': ['WARRIOR OF THE INTERNET', 3, 2, 3, 2, 3], 'B009': ['LAGARTO ELÉCTRICO', 4, 1, 2, 4, 3], 'B010': ['MECANIC DRON', 5, 5, 1, 1, 3], 'B011': ['LAZER MORTAL', 1, 2, 4, 3, 5], 'B012': ['MOTHER BOARD FROM HELL', 2, 4, 5, 0, 5], 'B013': ['COMPUTER FROM HEAVEN', 3, 2, 3, 4, 5], 'B014': ['VAPORWAVE DJ', 4, 3, 4, 2, 5], 'B015': ['BENDER', 5, 2, 9, 0, 7]}

class Player:
    def __init__(self, Player_name, Player_cards, Player_blood = 0,  plus_vid = True, plus_blood = True, nul_card = True, card_conv = 3):
        self.name = Player_name
        self.n_cards = Player_cards
        self.n_blood = Player_blood
        self.power_vid = plus_vid
        self.power_blood = plus_blood
        self.power_card = nul_card
        self.Cards = []
        self.conv_num = card_conv
    
    def ataque(self, TableroP1, TableroP2, Card):
        if(TableroP1.Spac_1 == True):
            if (TableroP2.Spac_1 == True):
                A = TableroP1.P_Cards[1]
                B = TableroP2.P_Cards[1]
                # restar damage de escudo y guardar 
                # si escudo en B es <= 0 eliminar
            else:
                A = TableroP1.P_Cards[1]
                # sumar ataque a damage del tablero contrincante
        else:
    
        if(TableroP1.Spac_2 == True):
            if (TableroP2.Spac_2 == True):
                A = TableroP1.P_Cards[2]
                B = TableroP2.P_Cards[2]
                # restar damage de escudo y guardar 
                # si escudo en B es <= 0 eliminar
            else:
                A = TableroP1.P_Cards[2]
                # sumar ataque a damage del tablero contrincante
        else:

        if(TableroP1.Spac_3 == True):
            if (TableroP2.Spac_3 == True):
                CartaA = TableroP1.P_Cards[3]
                CartaB = TableroP2.P_Cards[3]
                # restar damage de escudo y guardar 
                # si escudo en B es <= 0 eliminar
            else:
                CartaA = TableroP1.P_Cards[3]
                # sumar ataque a damage del tablero contrincante
        else:
        
        self.conv_num = 3 ## Contador de convocados disponibles
        TableroP1.turn += 1


    
    def convocar(self, TableroP1, Card1, Card2, Card3, MazoP1, playerP1):
        
        contador_1 = 0
        esp_card = input("ID de la carta a convocar: ")
        prop_carta = cartas_DISP.get(esp_card, "la carta no existe") ##brak si no existe un if?

        while contador_1 == 0:
            
            # evaluar la carta en selve.cards o lista de cartas disponibles para ver si se puede continuar dejar un marcador para meter con un operador "or" en cada IF

            esp_tablero = int(input("espacio 1 2 ó 3 donde poner la carta: "))

            if prop_carta [5] >= self.n_blood:
                if esp_tablero == 1:
                    if TableroP1.Spac_1 == False:
                        TableroP1.Spac_1 = True
                        TableroP1.P_cards [0] = esp_card
                        Card1.ID = esp_card
                        Card1.name = prop_carta [0]
                        Card1.damage = prop_carta [2]
                        Card1.shield = prop_carta [3]
                        Card1.blood = prop_carta [4]
                        Mazo.num1_car -= 1
                        self.conv_num -= 1
                        contador_1 = 1
                        self.nblod -= prop_carta [5]
                        # quitar la carta de la lista de cartas disponibles
                    else :
                        print ("el espacio 1 ya se encuentra ocupado")
                
                elif esp_tablero == 2:
                    if TableroP1.Spac_2 == False:
                        TableroP1.Spac_2 = True
                        TableroP1.P_cards [1] = esp_card
                        Card2.ID = esp_card
                        Card2.name = prop_carta [0]
                        Card2.damage = prop_carta [2]
                        Card2.shield = prop_carta [3]
                        Card2.blood = prop_carta [4]
                        Mazo.num1_car -= 1
                        self.conv_num -= 1
                        contador_1 = 1
                        self.nblod -= prop_carta [5]
                    else :
                        print ("el espacio 2 ya se encuentra ocupado")

                elif esp_tablero == 3:
                    if TableroP1.Spac_3 == False:
                        TableroP1.Spac_3 = True
                        TableroP1.P_cards [2] = esp_card
                        Card3.ID = esp_card
                        Card3.name = prop_carta [0]
                        Card3.damage = prop_carta [2]
                        Card3.shield = prop_carta [3]
                        Card3.blood = prop_carta [4]
                        Mazo.num1_car -= 1
                        self.conv_num -= 1
                        contador_1 = 1
                        self.nblod -= prop_carta [5]
                    else :
                        print ("el espacio 3 ya se encuentra ocupado")

    def sacrificar(self, TableroP1, Card1, Card2, Card3, MazoP1, playerP1):
        contador_2 = 0
        esp_card = input("ID de la carta a sacrificar: ")
        prop_carta = cartas_DISP.get(esp_card, "la carta no existe") ##brak si no existe un if?

        while contador_1 == 0:

            if esp_card == Card1.ID:
                TableroP1.Spac_1 = False
                TableroP1.P_cards [0] = 0
                Card1.ID = 0
                Card1.name = 0
                Card1.damage = 0
                Card1.shield = 0
               Card1.blood = 0
                self.blood += prop_carta [5]
                contador_2 = 1

            elif esp_card == Card2.ID:
                TableroP1.Spac_2 = False
                TableroP1.P_cards [1] = 0
                Card2.ID = 0
                Card2.name = 0
                Card2.damage = 0
                Card2.shield = 0
                Card2.blood = 0
                self.blood += prop_carta [5]
                contador_2 = 1

            elif esp_card == Card3.ID:
                TableroP1.Spac_3 = False
                TableroP1.P_cards [2] = 0
                Card3.ID = 0
                Card3.name = 0
                Card3.damage = 0
                Card3.shield = 0
                Card3.blood = 0
                self.blood += prop_carta [5]
                contador_2 = 1
        
            else:
                print("la carta no se encuentra de tu lado del tablero")



class Card:
    def __init__(self, Card_ID, Card_name, Card_damage, Cars_shield, Card_blood, Card_X):
        self.ID = Card_ID
        self.name = Card_name
        self.damage = Card_damage
        self.shield = Cars_shield
        self.blood = Card_blood
        self.sacri = Card_X

class Side_table:
    def __init__(self, Card_1P = False, Card_2P = False, Card_3P = False, Player_vid = 0; turnop1 = 0):
        self.Spac_1 = Card_1P
        self.Spac_2 = Card_2P
        self.Spac_3 = Card_3P
        self.Play_vid = Player_vid
        self.turn = turnop1
        self.P_Cards = ["", "", ""]

class Mazo:
    def __init__(self, Num_car = 30, Num_sac = 15):
        self.num1_car = Num_car
        self.num1_sacrificio = Num_sac



