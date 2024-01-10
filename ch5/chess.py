def isValidChessBoard(chess_dict: dict[str,str]) -> bool:
    piece_quant = {'wpawn': 0, 'bpawn': 0, 'wking': 0, 'bking': 0}
    w_pieces = 0
    b_pieces = 0

    for coord, piece in chess_dict.items():
        # print(coord)
        # print(piece[1:])

        if len(coord) != 2:
            # print("Failed check1")
            return False
        if coord[0] not in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            # print("Failed check2")
            return False
        if int(coord[1]) < 1 or int(coord[1]) > 8:
            # print("Failed check3")
            return False
                
        if piece[0] != 'w' and piece[0] != 'b':
            # print("Failed check4")
            return False
        if piece[1:] not in ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']:
            # print("Failed check5")
            return False
        
        if piece not in piece_quant:
            piece_quant[piece] = 1
        else:
            piece_quant[piece] += 1

    # print(piece_quant)

    for piece, quant in piece_quant.items():
        if piece[0] == 'w':
            w_pieces = w_pieces + quant
        else:
            b_pieces = b_pieces + quant

    # print(w_pieces)
    # print(b_pieces)

    if w_pieces > 16 or b_pieces > 16:
        # print("Failed check6")
        return False
    
    if piece_quant['wpawn'] > 8 or piece_quant['bpawn'] > 8:
        # print("Failed check7")
        return False
    
    if piece_quant['wking'] != 1 or piece_quant['bking'] != 1:
        # print("Failed check8")
        return False
    
    return True
    # print("Valid")

#Tests:

TestDict = { 
'dict0': {'a1': 'wpawn',
         'h2': 'wpawn',
         'd3': 'wpawn',
         'f1': 'wpawn',
         'b8': 'wpawn',
         'd5': 'wpawn',
         'h8': 'wpawn',
         'c7': 'wpawn',
         'f3': 'wrook',
         'c1': 'wrook',
         'd8': 'wqueen',
         'b3': 'wbishop',
         'b6': 'wbishop',
         'a7': 'wknight',
         'a5': 'wknight',
         'g6': 'bking',
         'f2': 'wking'
         },

#wrong coordinates
'dict1':{'z1': 'wpawn',
         'h2': 'bpawn',
         'g6': 'wking',
         'f2': 'bking'
         },

'dict2':{'a1': 'wpawn',
         'h2': 'bpawn',
         'g9': 'wking',
         'f2': 'bking'
         },

'dict3':{'a1': 'wpawn',
         'h2': 'bpawn',
         'g6': 'wking',
         'abc': 'bking'
         },

#wrong piecenames
'dict4':{'a1': 'wpan',
         'h2': 'bpawn',
         'g6': 'wking',
         'f2': 'bking'
         },

'dict5':{'a1': 'wpawn',
         'h2': 'xpawn',
         'g6': 'wking',
         'f2': 'bking'
         },


#wrong number of kings
'dict6':{'a1': 'wpawn',
         'h2': 'bpawn',
         'g6': 'wking',
         'f2': 'wking'
         },

'dict7':{'a1': 'wpawn',
         'h2': 'bpawn',
         'g6': 'wqueen',
         'f2': 'bqueen'
         },


#wrong number of pawns
'dict8':{'a1': 'wpawn',
         'h2': 'wpawn',
         'd3': 'wpawn',
         'f1': 'wpawn',
         'b8': 'wpawn',
         'd5': 'wpawn',
         'h8': 'wpawn',
         'c7': 'wpawn',
         'f3': 'wpawn',
         'g6': 'bking',
         'f2': 'wking'
         },

'dict9':{'a1': 'wpawn',
         'h2': 'wpawn',
         'd3': 'wpawn',
         'f1': 'wpawn',
         'b8': 'wpawn',
         'd5': 'wpawn',
         'h8': 'wpawn',
         'c7': 'wpawn',
         'f3': 'wrook',
         'c1': 'wrook',
         'd8': 'wqueen',
         'c2': 'wqueen',
         'b3': 'wbishop',
         'b6': 'wbishop',
         'a7': 'wknight',
         'a5': 'wknight',
         'g6': 'bking',
         'f2': 'wking'
         }
}


for test, dictionary in TestDict.items():
    print(f'The result of {test} is {isValidChessBoard(dictionary)}')