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


# +
def symetrie(mat):
    return mat[::-1]

def rotate_90(mat):
    return symetrie(mat.T)

def add_orientation(orient, orients):
    if orient not in orients:
        orients.append(orient)
    return None

def orientations(shape):
    orientations = []
    add_orientation(shape, orientations)

    ## on ajoute les rotations
    rotated_90 = rotate_90(shape)
    add_orientation(rotated_90, orientations)

    rotated_180 = rotate_90(rotated_90)
    add_orientation(rotated_180, orientations)

    rotated_270 = rotate_90(rotated_180)
    add_orientation(rotated_270, orientations)

    ## on ajoute la symétrie et ses rotations
    reflected = symetrie(shape)
    add_orientation(reflected, orientations)
        
    rotated_90r = rotate_90(reflected)
    add_orientation(rotated_90r, orientations)

    rotated_180r = rotate_90(rotated_90r)
    add_orientation(rotated_180r, orientations)

    rotated_270r = rotate_90(rotated_180r)
    add_orientation(rotated_270r, orientations)

def positions(board):
    position = np.array([])
    for name, cells in PENTOMINOS.items():
        current = cell


# -

# rectangles
BOARD_3_20 = np.zeros((3, 20), dtype=bool)
BOARD_4_15 = np.zeros((4, 15), dtype=bool)
BOARD_5_12 = np.zeros((5, 12), dtype=bool)
BOARD_6_10 = np.zeros((6, 10), dtype=bool)

# 8x8 with a 2x2 hole in the middle
BOARD_8_8 = np.zeros((8, 8), dtype=bool)
BOARD_8_8[3:5, 3:5] = 1

# 2 separate 3x10 rectangles
# has no solution
NO_BOARD_2_3_10 = np.zeros((3, 21), dtype=DTYPE)
NO_BOARD_2_3_10[:, 10] = 1

# 2 separate 5x6 rectangles
BOARD_2_5_6 = np.zeros((5, 13), dtype=DTYPE)
BOARD_2_5_6[:, 6] = 1

# 3 separate 4x5 rectangles
# has no solution
NO_BOARD_3_4_5 = np.zeros((3, 23), dtype=DTYPE)
NO_BOARD_3_4_5[:, 5:6] = 1

BOARD_8_9 = np.zeros((8, 9), dtype=DTYPE)
BOARD_8_9[::7, ::8] = 1
BOARD_8_9[1::5, ::8] = 1
BOARD_8_9[::7, 1::6] = 1

SMALL_BOARD = np.array([[1, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=DTYPE)
SMALL_PIECE = np.array([[0, 1], [1, 1]], dtype=DTYPE)
