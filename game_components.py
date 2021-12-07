import pandas as pd
import pprint
pp = pprint.PrettyPrinter(width=300)


def to_graph_notation(python_position):
    grid_to_graph_notation = [
    ['[1,8]','[2,8]','[3,8]','[4,8]','[5,8]','[6,8]','[7,8]','[8,8]'],
    ['[1,7]','[2,7]','[3,7]','[4,7]','[5,7]','[6,7]','[7,7]','[8,7]'],
    ['[1,6]','[2,6]','[3,6]','[4,6]','[5,6]','[6,6]','[7,6]','[8,6]'],
    ['[1,5]','[2,5]','[3,5]','[4,5]','[5,5]','[6,5]','[7,5]','[8,5]'],
    ['[1,4]','[2,4]','[3,4]','[4,4]','[5,4]','[6,4]','[7,4]','[8,4]'],
    ['[1,3]','[2,3]','[3,3]','[4,3]','[5,3]','[6,3]','[7,3]','[8,3]'],
    ['[1,2]','[2,2]','[3,2]','[4,2]','[5,2]','[6,2]','[7,2]','[8,2]'],
    ['[1,1]','[2,1]','[3,1]','[4,1]','[5,1]','[6,1]','[7,1]','[8,1]']
    ]
    x = python_position[1]
    y = python_position[0]
    return f'graph notation - {grid_to_graph_notation[y][x]}'


def to_chess_notation(python_position):
    grid_to_chess_notation = [
        ['a8','b8','c8','d8','e8','f8','g8','h8'],
        ['a7','b7','c7','d7','e7','f7','g7','h7'],
        ['a6','b6','c6','d6','e6','f6','g6','h6'],
        ['a5','b5','c5','d5','e5','f5','g5','h5'],
        ['a4','b4','c4','d4','e4','f4','g4','h4'],
        ['a3','b3','c3','d3','e3','f3','g3','h3'],
        ['a2','b2','c2','d2','e2','f2','g2','h2'],
        ['a1','b1','c1','d1','e1','f1','g1','h1'],
    ]
    x = python_position[1]
    y = python_position[0]
    return f'chess notation - {grid_to_chess_notation[y][x]}'

def check_for_checkmate(color):
    # to check if a color is in checkmate
    pass
    #if 
    #king.is_threatened():
    



def positions_being_attacked_by_opponent(opponent_color, board):

    flatten_board = []
    opponent_pieces = []
    self_pieces = []

    positions_being_attacked = dict()
  
  ## review this - seems inefficient
    for sublist in board:
        for val in sublist:
            flatten_board.append(val)

    all_pieces = [piece for piece in flatten_board if piece]
    for piece in all_pieces:
        if piece.color == opponent_color:
            opponent_pieces.append(piece)
        else:
            self_pieces.append(piece)


    print(f'the opponent pieces are {opponent_pieces}')
    # now we get all of the attack positions for the opponent

    for piece in opponent_pieces:
        piece_moves, pawn_moves, pawn_attack_moves = possible_moves(piece,board)
        attack_moves = piece_moves + pawn_attack_moves
        for move in attack_moves:
            positions_being_attacked[str(move)] = positions_being_attacked.get(str(move), 0) + 1

    pprint.pprint(positions_being_attacked)





class Piece:
    def __init__(self, form, position, color):
        self.color = color
        self.form = form
        self.position = position

    def __repr__ (self):
        return self.color + self.form
    
def possible_moves(piece, board):
    # OUTPUT is PYTHON FORMAT
    piece_moves = [] # this does not include pawns
    pawn_moves = []
    pawn_attack_moves = []

    # // TODO - Make an attack_moves list --- this can come from the line where we check if .color != piece.color
    xpos_python = piece.position[1]
    ypos_python = piece.position[0]

    if piece.form == 'rook':
        #     # Check to the Right
        for _ in range(xpos_python+1,8):
            print('testing')
            if board[ypos_python][_] == None:
                piece_moves.append([ypos_python,_])
            elif board[ypos_python][_].color != piece.color:
                piece_moves.append([ypos_python,_])
                break
            else:
                # defend_move.append()
                break

        ### this has to work backwards --- like start checking at the left
        for _ in reversed(range(0,xpos_python)):   
            if board[ypos_python][_] == None:
                piece_moves.append([ypos_python,_])
            elif board[ypos_python][_].color != piece.color:
                piece_moves.append([ypos_python,_])
                break
            else:
                break    

        ## check rook moves down
        for _ in range(ypos_python+1,8):
            if board[_][xpos_python] == None:
                piece_moves.append([_,xpos_python])
            elif board[_][xpos_python].color != piece.color:
                # print(f'Enemy piece - {board[_][xpos_python]} at {to_chess_notation(board[_][xpos_python].position)}') #this can be added as a debug to move in any direction //TODO
                piece_moves.append([_,xpos_python])
                break
            else:
                break    

        ## check rook moves up
        for _ in reversed(range(0,ypos_python)):
            if board[_][xpos_python] == None:
                piece_moves.append([_,xpos_python])
            elif board[_][xpos_python].color != piece.color:
                piece_moves.append([_,xpos_python])
                break
            else:
                break 
        print(f'rook moves are {[to_chess_notation(move) for move in piece_moves]}')   

    if piece.form == 'king':
        print('getting king moves')
        for row in range(ypos_python-1,ypos_python+2):
            if 0 <= row < 8:
                for column in range(xpos_python-1,xpos_python+2):
                    if 0 <= column < 8:
                        # print(f'testing python list - {[row,column]} as possible position') #debug
                        if piece.position != [row, column]:
                            if not board[row][column]:
                                piece_moves.append([row,column])
                            elif board[row][column].color != piece.color:
                                piece_moves.append([row,column])
                            else:
                                continue
        print(f'king moves are {[to_chess_notation(move) for move in piece_moves]}')                
    
    if piece.form != 'pawn':
        #must fill in with pawn_variables
        pass
    else:
        pass

    # print([[to_graph_notation(move) for move in piece_moves]])
    # print(f'{piece.form} {piece.color}' )
    return piece_moves, pawn_moves, pawn_attack_moves


def create_new_game_pieces(board):
    white_pieces = []
    black_pieces = []

    # for _ in range(0,8):
    #     white_pieces.append(Piece('pawn',[6,_],'white'))
    # white_pieces.append(Piece('rook',[1,6],'white'))
    # white_pieces.append(Piece('rook',[7,0],'white'))
    # white_pieces.append(Piece('knight',[7,1],'white'))
    # white_pieces.append(Piece('bishop',[7,2],'white'))
    white_pieces.append(Piece('king',[7,3],'white'))
    # white_pieces.append(Piece('queen',[7,4],'white'))
    # white_pieces.append(Piece('bishop',[7,5],'white'))
    # white_pieces.append(Piece('knight',[7,6],'white'))
    # white_pieces.append(Piece('rook',[7,7],'white'))

    # for _ in range(0,4):
    #     black_pieces.append(Piece('pawn',[1,_],'black'))

    black_pieces.append(Piece('king',[0,6],'black'))
    # black_pieces.append(Piece('rook',[0,0],'black'))
    # black_pieces.append(Piece('knight',[0,1],'black'))
    # black_pieces.append(Piece('bishop',[0,2],'black'))
    # black_pieces.append(Piece('king',[0,3],'black'))
    # black_pieces.append(Piece('queen',[0,4],'black'))
    # black_pieces.append(Piece('bishop',[0,5],'black'))
    # black_pieces.append(Piece('knight',[0,6],'black'))
    black_pieces.append(Piece('rook',[0,7],'black'))



    print(f'white pieces generated --- {white_pieces}')
    print(f'black pieces generated --- {black_pieces}')
    print()

    for piece in white_pieces:
        board[piece.position[0]][piece.position[1]] = piece

    for piece in black_pieces:
        board[piece.position[0]][piece.position[1]] = piece

    return board


new_board =  [[None] * 8 for _ in range(8)]



new_board = create_new_game_pieces(new_board)

# print(possible_moves(new_board[3][4],new_board))
positions_being_attacked_by_opponent('black', new_board)


pp.pprint(new_board)
df = pd.DataFrame(new_board)
## // TODO make a column to add the axis labels
df.to_excel('result.xlsx', index = False)

# print(br1.position)
# print(possible_moves(br1, new_board))




