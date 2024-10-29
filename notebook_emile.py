import numpy as np
import matplotlib.pyplot as plt
import xcover

RAW_SHAPES = {
    "F": np.array([[1, 1, 0], 
                   [0, 1, 1], 
                   [0, 1, 0]]),

    "I": np.array([[1, 1, 1, 1, 1]]),

    "L": np.array([[1, 0, 0, 0], 
                   [1, 1, 1, 1]]),

    "N": np.array([[1, 1, 0, 0], 
                   [0, 1, 1, 1]]),

    "P": np.array([[1, 1, 1], 
                   [1, 1, 0]]),

    "T": np.array([[1, 1, 1], 
                   [0, 1, 0], 
                   [0, 1, 0]]),

    "U": np.array([[1, 1, 1], 
                   [1, 0, 1]]),

    "V": np.array([[1, 1, 1], 
                   [1, 0, 0], 
                   [1, 0, 0]]),

    "W": np.array([[1, 0, 0], 
                   [1, 1, 0], 
                   [0, 1, 1]]),

    "X": np.array([[0, 1, 0], 
                   [1, 1, 1], 
                   [0, 1, 0]]),

    "Y": np.array([[0, 1, 0, 0], 
                   [1, 1, 1, 1]]),

    "Z": np.array([[1, 1, 0], 
                   [0, 1, 0], 
                   [0, 1, 1]]),
}

# rectangles
BOARD_3_20 = np.zeros((3, 20))
BOARD_4_15 = np.zeros((4, 15))
BOARD_5_12 = np.zeros((5, 12))
BOARD_6_10 = np.zeros((6, 10))

# 8x8 with a 2x2 hole in the middle
BOARD_8_8 = np.zeros((8, 8))
BOARD_8_8[3:5, 3:5] = 1

# 2 separate 3x10 rectangles
# has no solution
NO_BOARD_2_3_10 = np.zeros((3, 21))
NO_BOARD_2_3_10[:, 10] = 1

# 2 separate 5x6 rectangles
BOARD_2_5_6 = np.zeros((5, 13))
BOARD_2_5_6[:, 6] = 1

# 3 separate 4x5 rectangles
# has no solution
NO_BOARD_3_4_5 = np.zeros((3, 23))
NO_BOARD_3_4_5[:, 5:6] = 1

BOARD_8_9 = np.zeros((8, 9))
BOARD_8_9[::7, ::8] = 1
BOARD_8_9[1::5, ::8] = 1
BOARD_8_9[::7, 1::6] = 1


# Déplacer les lettres dans le tableau

def initialisation(board,letter):
    liste_board = []
    boardc = np.copy(board)
    boardc[:len(letter),:len(letter[0])] = letter
    liste_board.append(boardc.reshape(60))
    return liste_board
# print(initialisation(BOARD_6_10,RAW_SHAPES["F"]))


# Nouvelle tentative
def translation(board,letter):
    liste_board = initialisation(board,letter)
    
    tableau_trans = liste_board[0].reshape(np.shape(board))

    while 1 not in tableau_trans[:,-1].tolist():

        trans = np.array([0] + liste_board[-1].tolist())
        trans = trans[:-1]
        tableau_trans = np.array(trans).reshape(np.shape(board))
        liste_board.append(trans)
        
    return liste_board

initi = translation(BOARD_6_10,RAW_SHAPES["F"])
print(initi)


def descente(board,letter):
    liste_board = translation(board,letter)
    n = len(liste_board)
    zeros = [0 for i in range(np.shape(board)[1])]

    while np.array(liste_board[-1][-np.shape(board)[1]:]).any() != 1:
        L = []
        for i in range(n):
            trans = np.array(zeros + liste_board[-i].tolist())
            trans= trans[:-10]
            L.append(trans)
        liste_board.append(L)
    return(liste_board)

complet = descente(BOARD_6_10,RAW_SHAPES["F"])
print(complet)


    





