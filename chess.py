import random

chessboard = [
    ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
    ['♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎', '♟︎'],
    ['·', '·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·', '·'],
    ['·', '·', '·', '·', '·', '·', '·', '·'],
    ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
    ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
]

def usermove():
    while True:
        userinput1 = input('Choose the Piece you want to move (e2): ').lower()
        print('\n')
        inputlist1 = list(userinput1)
        if len(inputlist1) == 2:
            if inputlist1[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                if inputlist1[1] in ['1', '2', '3', '4', '5', '6', '7', '8']:
                    break
                else:
                    print('ERROR! INVALID INPUT!\n\n')
            else:
                print('ERROR! INVALID INPUT!\n\n')
        else:
            print('ERROR! INVALID INPUT!\n\n')
    while True:
        userinput2 = input('Where do you want to move your Piece (e4): ').lower()
        print('\n')
        inputlist2 = list(userinput2)
        if len(inputlist2) == 2:
            if inputlist2[0] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
                if inputlist2[1] in ['1', '2', '3', '4', '5', '6', '7', '8']:
                    usermove = inputlist1.append(inputlist2)
                    if usermove in check_moves(chessboard):
                        break
                    else:
                            print('Move not possible!\n\n')
                else:
                        print('ERROR! INVALID INPUT!\n\n')
            else:
                    print('ERROR! INVALID INPUT!\n\n')
        else:
                print('ERROR! INVALID INPUT!\n\n')
    chessboard[usermove[2]][usermove[3]] = chessboard[usermove[0]][usermove[1]]
    chessboard[usermove[0]][usermove[1]] = '·'

while True:
    start_position = input('Would you like to play with white or with black? (w/b): ').lower()
    print('\n')
    if start_position in ['w', '(w)', 'white']:

        white = True
        def printposition():
            print('8   ' + chessboard[0][0] + '   ' + chessboard[0][1] + '   ' + chessboard[0][2] + '   ' + chessboard[0][3] + '   ' + 
                  chessboard[0][4] + '   ' + chessboard[0][5] + '   ' + chessboard[0][6] + '   ' + chessboard[0][7] + '\n' + '\n' 
                  '7   ' + chessboard[1][0] + '   ' + chessboard[1][1] + '   ' + chessboard[1][2] + '   ' + chessboard[1][3] + '   ' + 
                  chessboard[1][4] + '   ' + chessboard[1][5] + '   ' + chessboard[1][6] + '   ' + chessboard[1][7] + '\n' + '\n'
                  '6   ' + chessboard[2][0] + '   ' + chessboard[2][1] + '   ' + chessboard[2][2] + '   ' + chessboard[2][3] + '   ' + 
                  chessboard[2][4] + '   ' + chessboard[2][5] + '   ' + chessboard[2][6] + '   ' + chessboard[2][7] + '\n' + '\n'
                  '5   ' + chessboard[3][0] + '   ' + chessboard[3][1] + '   ' + chessboard[3][2] + '   ' + chessboard[3][3] + '   ' + 
                  chessboard[3][4] + '   ' + chessboard[3][5] + '   ' + chessboard[3][6] + '   ' + chessboard[3][7] + '\n' + '\n'
                  '4   ' + chessboard[4][0] + '   ' + chessboard[4][1] + '   ' + chessboard[4][2] + '   ' + chessboard[4][3] + '   ' + 
                  chessboard[4][4] + '   ' + chessboard[4][5] + '   ' + chessboard[4][6] + '   ' + chessboard[4][7] + '\n' + '\n'
                  '3   ' + chessboard[5][0] + '   ' + chessboard[5][1] + '   ' + chessboard[5][2] + '   ' + chessboard[5][3] + '   ' + 
                  chessboard[5][4] + '   ' + chessboard[5][5] + '   ' + chessboard[5][6] + '   ' + chessboard[5][7] + '\n' + '\n'
                  '2   ' + chessboard[6][0] + '   ' + chessboard[6][1] + '   ' + chessboard[6][2] + '   ' + chessboard[6][3] + '   ' + 
                  chessboard[6][4] + '   ' + chessboard[6][5] + '   ' + chessboard[6][6] + '   ' + chessboard[6][7] + '\n' + '\n'
                  '1   ' + chessboard[7][0] + '   ' + chessboard[7][1] + '   ' + chessboard[7][2] + '   ' + chessboard[7][3] + '   ' + 
                  chessboard[7][4] + '   ' + chessboard[7][5] + '   ' + chessboard[7][6] + '   ' + chessboard[7][7] + '\n' + '\n'
                  '    a   b   c   d   e   f   g   h\n\n') 

        def check_moves(chessboard):
            moves = []
            rownumber = 0
            for row in chessboard:
                itemnumber = 0
                for item in row:

                    if item == '♖':
                        
                        #check right
                        range_itemnumber = itemnumber + 1
                        while 0 <= range_itemnumber <= 7:
                            if chessboard[rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                            elif chessboard[rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber + 1

                        #check left
                        range_itemnumber = itemnumber - 1
                        while 0 <= range_itemnumber <= 7:
                            if chessboard[rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                            elif chessboard[rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber - 1

                        #check down
                        range_rownumber = rownumber + 1
                        while 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                            elif chessboard[range_rownumber][itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                                break
                            else:
                                break
                            range_rownumber = range_rownumber + 1

                        #check up
                        range_rownumber = rownumber - 1
                        while 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                            elif chessboard[range_rownumber][itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                                break
                            else:
                                break
                            range_rownumber = range_rownumber - 1

                    elif item == '♘':

                        while 0 <= itemnumber + 2 <= 7 and 0 <= rownumber + 1 <= 7:
                            if chessboard[rownumber + 1][itemnumber + 2] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber + 2])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber + 2])
                                break
                            else:
                                break

                        while 0 <= itemnumber + 1 <= 7 and 0 <= rownumber + 2 <= 7:
                            if chessboard[rownumber + 2][itemnumber + 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 2, itemnumber + 1])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber + 2, itemnumber + 1])
                                break
                            else:
                                break

                        while 0 <= itemnumber + 2 <= 7 and 0 <= rownumber - 1 <= 7:
                            if chessboard[rownumber - 1][itemnumber + 2] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber + 2])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber + 2])
                                break
                            else:
                                break

                        while 0 <= itemnumber + 1 <= 7 and 0 <= rownumber - 2 <= 7:
                            if chessboard[rownumber - 2][itemnumber + 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 2, itemnumber + 1])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber - 2, itemnumber + 1])
                                break
                            else:
                                break

                        while 0 <= itemnumber - 1 <= 7 and 0 <= rownumber + 2 <= 7:
                            if chessboard[rownumber + 2][itemnumber - 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 2, itemnumber - 1])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber + 2, itemnumber - 1])
                                break
                            else:
                                break

                        while 0 <= itemnumber - 2 <= 7 and 0 <= rownumber + 1 <= 7:
                            if chessboard[rownumber + 1][itemnumber - 2] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber - 2])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber - 2])
                                break
                            else:
                                break

                        while 0 <= itemnumber - 2 <= 7 and 0 <= rownumber - 1 <= 7:
                            if chessboard[rownumber - 1][itemnumber - 2] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber - 2])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber - 2])
                                break
                            else:
                                break

                        while 0 <= itemnumber - 1 <= 7 and 0 <= rownumber - 2 <= 7:
                            if chessboard[rownumber - 2][itemnumber - 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 2, itemnumber - 1])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber - 2, itemnumber - 1])
                                break
                            else:
                                break

                    elif item == '♗':

                        #check right - down
                        range_itemnumber = itemnumber + 1
                        range_rownumber = rownumber + 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber + 1
                            range_rownumber = range_rownumber + 1

                        #check left - down
                        range_itemnumber = itemnumber + 1
                        range_rownumber = rownumber - 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber + 1
                            range_rownumber = range_rownumber - 1

                        #check left - top
                        range_itemnumber = itemnumber - 1
                        range_rownumber = rownumber + 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber - 1
                            range_rownumber = range_rownumber + 1

                        #check right - top
                        range_itemnumber = itemnumber - 1
                        range_rownumber = rownumber - 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber - 1
                            range_rownumber = range_rownumber - 1

                    elif item == '♙':

                        if chessboard[rownumber - 1][itemnumber] == '·':
                            moves.append([rownumber, itemnumber, rownumber - 1, itemnumber])
                        if rownumber == 6 and chessboard[rownumber - 2][itemnumber] == '·':
                            moves.append([rownumber, itemnumber, rownumber - 2, itemnumber])
                        if chessboard[rownumber - 1][itemnumber - 1] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                            moves.append([rownumber, itemnumber, rownumber - 1, itemnumber - 1])
                        if chessboard[rownumber - 1][itemnumber + 1] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                            moves.append([rownumber, itemnumber, rownumber - 1, itemnumber + 1])
                        else:
                            break

                    elif item == '♔':

                        #check right
                        while 0 <= itemnumber  + 1 <= 7:
                            if chessboard[rownumber][itemnumber + 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber, itemnumber + 1])
                            elif chessboard[rownumber][itemnumber + 1] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber, itemnumber + 1])
                                break
                            else:
                                break

                        #check left
                        while 0 <= itemnumber  - 1 <= 7:
                            if chessboard[rownumber][itemnumber - 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber, itemnumber - 1])
                            elif chessboard[rownumber][itemnumber + 1] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber, itemnumber - 1])
                                break
                            else:
                                break

                        #check down
                        while 0 <= rownumber + 1 <= 7:
                            if chessboard[rownumber + 1][itemnumber] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber])
                            elif chessboard[rownumber + 1][itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber])
                                break
                            else:
                                break

                        #check up
                        while 0 <= rownumber - 1 <= 7:
                            if chessboard[rownumber - 1][itemnumber] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber])
                            elif chessboard[rownumber - 1][itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber])
                                break
                            else:
                                break

                        #check right - down
                        while 0 <= rownumber + 1 <= 7 and 0 <= itemnumber + 1 <= 7:
                            if chessboard[rownumber + 1][itemnumber + 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber + 1])
                            elif chessboard[rownumber + 1][itemnumber + 1] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber + 1])
                                break
                            else:
                                break

                        #check left - down
                        while 0 <= rownumber + 1 <= 7 and 0 <= itemnumber - 1 <= 7:
                            if chessboard[rownumber + 1][itemnumber - 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber - 1])
                            elif chessboard[rownumber + 1][itemnumber - 1] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber - 1])
                                break
                            else:
                                break

                        #check left - up
                        while 0 <= rownumber - 1 <= 7 and 0 <= itemnumber - 1 <= 7:
                            if chessboard[rownumber - 1][itemnumber - 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber - 1])
                            elif chessboard[rownumber - 1][itemnumber - 1] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber - 1])
                                break
                            else:
                                break

                        #check right - up
                        while 0 <= rownumber - 1 <= 7 and 0 <= itemnumber + 1 <= 7:
                            if chessboard[rownumber - 1][itemnumber + 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber + 1])
                            elif chessboard[rownumber - 1][itemnumber + 1] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber + 1])
                                break
                            else:
                                break

                    elif item == '♕':

                        #check right
                        range_itemnumber = itemnumber + 1
                        while 0 <= range_itemnumber <= 7:
                            if chessboard[rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                            elif chessboard[rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber + 1

                        #check left
                        range_itemnumber = itemnumber - 1
                        while 0 <= range_itemnumber <= 7:
                            if chessboard[rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                            elif chessboard[rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber - 1

                        #check down
                        range_rownumber = rownumber + 1
                        while 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                            elif chessboard[range_rownumber][itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                                break
                            else:
                                break
                            range_rownumber = range_rownumber + 1

                        #check up
                        range_rownumber = rownumber - 1
                        while 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                            elif chessboard[range_rownumber][itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                                break
                            else:
                                break
                            range_rownumber = range_rownumber - 1

                        #check right - down
                        range_itemnumber = itemnumber + 1
                        range_rownumber = rownumber + 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber + 1
                            range_rownumber = range_rownumber + 1

                        #check left - down
                        range_itemnumber = itemnumber + 1
                        range_rownumber = rownumber - 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber + 1
                            range_rownumber = range_rownumber - 1

                        #check left - top
                        range_itemnumber = itemnumber - 1
                        range_rownumber = rownumber + 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber - 1
                            range_rownumber = range_rownumber + 1

                        #check right - top
                        range_itemnumber = itemnumber - 1
                        range_rownumber = rownumber - 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♜', '♞', '♝', '♛', '♚', '♟︎']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber - 1
                            range_rownumber = range_rownumber - 1

                    itemnumber = itemnumber + 1
                rownumber = rownumber + 1
            return moves
        break

    if start_position in ['b', '(b)', 'black']:

        white = False
        def printposition():
            print('1   ' + chessboard[7][7] + '   ' + chessboard[7][6] + '   ' + chessboard[7][5] + '   ' + chessboard[7][4] + '   ' + 
                  chessboard[7][3] + '   ' + chessboard[7][2] + '   ' + chessboard[7][1] + '   ' + chessboard[7][0] + '\n' + '\n' 
                  '2   ' + chessboard[6][7] + '   ' + chessboard[6][6] + '   ' + chessboard[6][5] + '   ' + chessboard[6][4] + '   ' + 
                  chessboard[6][3] + '   ' + chessboard[6][2] + '   ' + chessboard[6][1] + '   ' + chessboard[6][0] + '\n' + '\n'
                  '3   ' + chessboard[5][7] + '   ' + chessboard[5][6] + '   ' + chessboard[5][5] + '   ' + chessboard[5][4] + '   ' + 
                  chessboard[5][3] + '   ' + chessboard[5][2] + '   ' + chessboard[5][1] + '   ' + chessboard[5][0] + '\n' + '\n'
                  '4   ' + chessboard[4][7] + '   ' + chessboard[4][6] + '   ' + chessboard[4][5] + '   ' + chessboard[4][4] + '   ' + 
                  chessboard[4][3] + '   ' + chessboard[4][2] + '   ' + chessboard[4][1] + '   ' + chessboard[4][0] + '\n' + '\n'
                  '5   ' + chessboard[3][7] + '   ' + chessboard[3][6] + '   ' + chessboard[3][5] + '   ' + chessboard[3][4] + '   ' + 
                  chessboard[3][3] + '   ' + chessboard[3][2] + '   ' + chessboard[3][1] + '   ' + chessboard[3][0] + '\n' + '\n'
                  '6   ' + chessboard[2][7] + '   ' + chessboard[2][6] + '   ' + chessboard[2][5] + '   ' + chessboard[2][4] + '   ' + 
                  chessboard[2][3] + '   ' + chessboard[2][2] + '   ' + chessboard[2][1] + '   ' + chessboard[2][0] + '\n' + '\n'
                  '7   ' + chessboard[1][7] + '   ' + chessboard[1][6] + '   ' + chessboard[1][5] + '   ' + chessboard[1][4] + '   ' + 
                  chessboard[1][3] + '   ' + chessboard[1][2] + '   ' + chessboard[1][1] + '   ' + chessboard[1][0] + '\n' + '\n'
                  '8   ' + chessboard[0][7] + '   ' + chessboard[0][6] + '   ' + chessboard[0][5] + '   ' + chessboard[0][4] + '   ' + 
                  chessboard[0][3] + '   ' + chessboard[0][2] + '   ' + chessboard[0][1] + '   ' + chessboard[0][0] + '\n' + '\n'
                  '    h   g   f   e   d   c   b   a\n\n') 

        def check_moves(chessboard):
            moves = []
            rownumber = 0
            for row in chessboard:
                itemnumber = 0
                for item in row:

                    if item == '♜':
                        
                        #check right
                        range_itemnumber = itemnumber + 1
                        while 0 <= range_itemnumber <= 7:
                            if chessboard[rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                            elif chessboard[rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber + 1

                        #check left
                        range_itemnumber = itemnumber - 1
                        while 0 <= range_itemnumber <= 7:
                            if chessboard[rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                            elif chessboard[rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber - 1

                        #check down
                        range_rownumber = rownumber + 1
                        while 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                            elif chessboard[range_rownumber][itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                                break
                            else:
                                break
                            range_rownumber = range_rownumber + 1

                        #check up
                        range_rownumber = rownumber - 1
                        while 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                            elif chessboard[range_rownumber][itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                                break
                            else:
                                break
                            range_rownumber = range_rownumber - 1

                    elif item == '♞':

                        while 0 <= itemnumber + 2 <= 7 and 0 <= rownumber + 1 <= 7:
                            if chessboard[rownumber + 1][itemnumber + 2] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber + 2])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber + 2])
                                break
                            else:
                                break

                        while 0 <= itemnumber + 1 <= 7 and 0 <= rownumber + 2 <= 7:
                            if chessboard[rownumber + 2][itemnumber + 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 2, itemnumber + 1])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber + 2, itemnumber + 1])
                                break
                            else:
                                break

                        while 0 <= itemnumber + 2 <= 7 and 0 <= rownumber - 1 <= 7:
                            if chessboard[rownumber - 1][itemnumber + 2] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber + 2])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber + 2])
                                break
                            else:
                                break

                        while 0 <= itemnumber + 1 <= 7 and 0 <= rownumber - 2 <= 7:
                            if chessboard[rownumber - 2][itemnumber + 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 2, itemnumber + 1])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber - 2, itemnumber + 1])
                                break
                            else:
                                break

                        while 0 <= itemnumber - 1 <= 7 and 0 <= rownumber + 2 <= 7:
                            if chessboard[rownumber + 2][itemnumber - 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 2, itemnumber - 1])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber + 2, itemnumber - 1])
                                break
                            else:
                                break

                        while 0 <= itemnumber - 2 <= 7 and 0 <= rownumber + 1 <= 7:
                            if chessboard[rownumber + 1][itemnumber - 2] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber - 2])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber - 2])
                                break
                            else:
                                break

                        while 0 <= itemnumber - 2 <= 7 and 0 <= rownumber - 1 <= 7:
                            if chessboard[rownumber - 1][itemnumber - 2] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber - 2])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber - 2])
                                break
                            else:
                                break

                        while 0 <= itemnumber - 1 <= 7 and 0 <= rownumber - 2 <= 7:
                            if chessboard[rownumber - 2][itemnumber - 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 2, itemnumber - 1])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber - 2, itemnumber - 1])
                                break
                            else:
                                break

                    elif item == '♝':

                        #check right - down
                        range_itemnumber = itemnumber + 1
                        range_rownumber = rownumber + 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber + 1
                            range_rownumber = range_rownumber + 1

                        #check left - down
                        range_itemnumber = itemnumber + 1
                        range_rownumber = rownumber - 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber + 1
                            range_rownumber = range_rownumber - 1

                        #check left - top
                        range_itemnumber = itemnumber - 1
                        range_rownumber = rownumber + 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber - 1
                            range_rownumber = range_rownumber + 1

                        #check right - top
                        range_itemnumber = itemnumber - 1
                        range_rownumber = rownumber - 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber - 1
                            range_rownumber = range_rownumber - 1

                    elif item == '♛':

                        #check right
                        range_itemnumber = itemnumber + 1
                        while 0 <= range_itemnumber <= 7:
                            if chessboard[rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                            elif chessboard[rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber + 1

                        #check left
                        range_itemnumber = itemnumber - 1
                        while 0 <= range_itemnumber <= 7:
                            if chessboard[rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                            elif chessboard[rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber - 1

                        #check down
                        range_rownumber = rownumber + 1
                        while 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                            elif chessboard[range_rownumber][itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                                break
                            else:
                                break
                            range_rownumber = range_rownumber + 1

                        #check up
                        range_rownumber = rownumber - 1
                        while 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                            elif chessboard[range_rownumber][itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, range_rownumber, itemnumber])
                                break
                            else:
                                break
                            range_rownumber = range_rownumber - 1

                        #check right - down
                        range_itemnumber = itemnumber + 1
                        range_rownumber = rownumber + 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber + 1
                            range_rownumber = range_rownumber + 1

                        #check left - down
                        range_itemnumber = itemnumber + 1
                        range_rownumber = rownumber - 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber + 1
                            range_rownumber = range_rownumber - 1

                        #check left - top
                        range_itemnumber = itemnumber - 1
                        range_rownumber = rownumber + 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber - 1
                            range_rownumber = range_rownumber + 1

                        #check right - top
                        range_itemnumber = itemnumber - 1
                        range_rownumber = rownumber - 1
                        while 0 <= range_itemnumber <= 7 and 0 <= range_rownumber <= 7:
                            if chessboard[range_rownumber][range_itemnumber] == '·':
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                            elif chessboard[range_rownumber][range_itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, range_rownumber, range_itemnumber])
                                break
                            else:
                                break
                            range_itemnumber = range_itemnumber - 1
                            range_rownumber = range_rownumber - 1

                    elif item == '♚':

                        #check right
                        while 0 <= itemnumber  + 1 <= 7:
                            if chessboard[rownumber][itemnumber + 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber, itemnumber + 1])
                            elif chessboard[rownumber][itemnumber + 1] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber, itemnumber + 1])
                                break
                            else:
                                break

                        #check left
                        while 0 <= itemnumber  - 1 <= 7:
                            if chessboard[rownumber][itemnumber - 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber, itemnumber - 1])
                            elif chessboard[rownumber][itemnumber + 1] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber, itemnumber - 1])
                                break
                            else:
                                break

                        #check down
                        while 0 <= rownumber + 1 <= 7:
                            if chessboard[rownumber + 1][itemnumber] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber])
                            elif chessboard[rownumber + 1][itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber])
                                break
                            else:
                                break

                        #check up
                        while 0 <= rownumber - 1 <= 7:
                            if chessboard[rownumber - 1][itemnumber] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber])
                            elif chessboard[rownumber - 1][itemnumber] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber])
                                break
                            else:
                                break

                        #check right - down
                        while 0 <= rownumber + 1 <= 7 and 0 <= itemnumber + 1 <= 7:
                            if chessboard[rownumber + 1][itemnumber + 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber + 1])
                            elif chessboard[rownumber + 1][itemnumber + 1] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber + 1])
                                break
                            else:
                                break

                        #check left - down
                        while 0 <= rownumber + 1 <= 7 and 0 <= itemnumber - 1 <= 7:
                            if chessboard[rownumber + 1][itemnumber - 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber - 1])
                            elif chessboard[rownumber + 1][itemnumber - 1] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber + 1, itemnumber - 1])
                                break
                            else:
                                break

                        #check left - up
                        while 0 <= rownumber - 1 <= 7 and 0 <= itemnumber - 1 <= 7:
                            if chessboard[rownumber - 1][itemnumber - 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber - 1])
                            elif chessboard[rownumber - 1][itemnumber - 1] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber - 1])
                                break
                            else:
                                break

                        #check right - up
                        while 0 <= rownumber - 1 <= 7 and 0 <= itemnumber + 1 <= 7:
                            if chessboard[rownumber - 1][itemnumber + 1] == '·':
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber + 1])
                            elif chessboard[rownumber - 1][itemnumber + 1] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                                moves.append([rownumber, itemnumber, rownumber - 1, itemnumber + 1])
                                break
                            else:
                                break

                    elif item == '♟︎':
                        if chessboard[rownumber + 1][itemnumber] == '·':
                            moves.append([rownumber, itemnumber, rownumber + 1, itemnumber])
                        if rownumber == 1 and chessboard[rownumber + 2][itemnumber] == '·':
                            moves.append([rownumber, itemnumber, rownumber + 2, itemnumber])
                        if chessboard[rownumber + 1][itemnumber + 1] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                            moves.append([rownumber, itemnumber, rownumber + 1, itemnumber + 1])
                        if chessboard[rownumber + 1][itemnumber - 1] in ['♖', '♘', '♗', '♕', '♔', '♙']:
                            moves.append([rownumber, itemnumber, rownumber + 1, itemnumber - 1])
                        else:
                            break

                    itemnumber = itemnumber + 1
                rownumber = rownumber + 1
            return moves
        break

    else:
        print('ERROR! INVALID INPUT!\n\n')

def check_position(chessboard):
    if len(check_moves(chessboard)) == 0:
        print('DRAW')
        return True
    else:
        if '♚' not in chessboard:
            print('White won!')
            return True
        else:
            if '♔' not in chessboard:
                print('Black won!')
                return True
            else:
                return False

if white:
    while True:
        printposition()
        usermove()
        if check_position(chessboard):
            break
        moves = check_moves(chessboard)
        computermove = check_moves(chessboard)[random.randrange(len(moves))]
        chessboard[computermove[2]][computermove[3]] = chessboard[computermove[0]][computermove[1]]
        chessboard[computermove[0]][computermove[1]] = '·'
        if check_position(chessboard):
            break
else:
    while True:
        moves = check_moves(chessboard)
        computermove = check_moves(chessboard)[random.randrange(len(moves))]
        chessboard[computermove[2]][computermove[3]] = chessboard[computermove[0]][computermove[1]]
        chessboard[computermove[0]][computermove[1]] = '·'
        if check_position(chessboard):
            break
        printposition()
        usermove()
        if check_position(chessboard):
            break