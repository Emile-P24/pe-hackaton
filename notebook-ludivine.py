pip install exact-cover

import xcover

import numpy as np

RAW_SHAPES = {
    "F": [[1, 1, 0], [0, 1, 1], [0, 1, 0]],
    "I": [[1, 1, 1, 1, 1]],
    "L": [[1, 0, 0, 0], [1, 1, 1, 1]],
    "N": [[1, 1, 0, 0], [0, 1, 1, 1]],
    "P": [[1, 1, 1], [1, 1, 0]],
    "T": [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
    "U": [[1, 1, 1], [1, 0, 1]],
    "V": [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
    "W": [[1, 0, 0], [1, 1, 0], [0, 1, 1]],
    "X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    "Y": [[0, 1, 0, 0], [1, 1, 1, 1]],
    "Z": [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
}

PENTOMINOS = [np.array(shape, dtype=bool) for shape in RAW_SHAPES.values()]


# On crée les fonctions permettant d'obtenir toutes les orientations possibles pour une figure donnée

# +
def symetrie(mat):
    return mat[::-1]

def rotate_90(mat):
    return symetrie(mat.T)

def add_orientation(orient, orients):
    for or_poss in orients :
        if np.array_equal(orient, or_poss) :
            return None
    orients.append(orient)
    return None

def orientations(shape):
    orient = []
    add_orientation(shape, orient)

    ## on ajoute les rotations
    rotated_90 = rotate_90(shape)
    add_orientation(rotated_90, orient)

    rotated_180 = rotate_90(rotated_90)
    add_orientation(rotated_180, orient)

    rotated_270 = rotate_90(rotated_180)
    add_orientation(rotated_270, orient)

    ## on ajoute la symétrie et ses rotations
    reflected = symetrie(shape)
    add_orientation(reflected, orient)
        
    rotated_90r = rotate_90(reflected)
    add_orientation(rotated_90r, orient)

    rotated_180r = rotate_90(rotated_90r)
    add_orientation(rotated_180r, orient)

    rotated_270r = rotate_90(rotated_180r)
    add_orientation(rotated_270r, orient)
    return orient


# -

# On crée la fonction permettant d'obtenir les positions possibles d'une figure dans le tableau global

# +
def tuple_to_number(position, board):
    h, l = board.shape
    x, y = position
    return (x*l)+y

def get_valid_positions(shape, board):
    h, l = board.shape
    
    valid_positions = []
    coords = [(x,y) for x in range(len(shape)) for y in range(len(shape[0])) if shape[x][y]==1]

    for gx in range(h):
        for gy in range(l):
            trans_coords = [(gx + cx, gy + cy) for cx, cy in coords]
            if all (0<= px < h and 0<= py < l for px, py in trans_coords):
                trans_coords = [tuple_to_number((px, py), board)  for px, py in trans_coords]
                letter_in_board = np.zeros((60,1))
                for coord in trans_coords :
                    letter_in_board[coord]=1
                valid_positions.append(letter_in_board)
    return valid_positions


# -

# On associe à l'aide d'un dictionnaire à chaque lettre sa liste associée (liste de 12 chiffres composées de 0 ou 1)

letters = np.array(["F", "I", "L", "N", "P", "T", "U", "V", "W", "X", "Y", "Z"])
letters_to_numbers = {}
for i in range (len(letters)):
    L = np.zeros((12,1))
    L[i] = 1
    letters_to_numbers[letters[i]] = L

# On associe à l'aide d'un dictionnaire à chaque liste (qui correspond donc à une lettre) la liste des positions possibles dans le tableau
# puis on met dans un tableau toutes les positions possibles pour toutes les lettres possibles

# +
positions_possibles = {}

def positions(board):
    for shape in PENTOMINOS:
        orient = orientations(shape)
        for orientation in orient :
            for e in letters_to_numbers.keys():
                if e not in positions_possibles.keys():
                    positions_possibles[e] = [get_valid_positions(orientation,board)]
                else :
                    positions_possibles[e].append(get_valid_positions(orientation,board))
    pos = []
    for key, value in positions_possibles.items():
        e = letters_to_numbers[key]
        for val in value :
            pos.append(np.concatenate((e.flatten(), np.array(val).flatten())))
    return pos


# -

# rectangles
BOARD_3_20 = np.zeros((3, 20), dtype=bool)
BOARD_4_15 = np.zeros((4, 15), dtype=bool)
BOARD_5_12 = np.zeros((5, 12), dtype=bool)
BOARD_6_10 = np.zeros((6, 10), dtype=bool)

# 8x8 with a 2x2 hole in the middle
BOARD_8_8 = np.zeros((8, 8), dtype=bool)
BOARD_8_8[3:5, 3:5] = 1

print(positions(BOARD_6_10))

# +
SMALL_BOARD = np.array([[1, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=bool)
PENTOMINOS = np.array([ np.array([[0, 1], [1, 1]], dtype=bool)])

print(positions(SMALL_BOARD))
# -


