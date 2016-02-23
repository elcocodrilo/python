## The game tic tac toe where you win by getting 3 of your pieces
## in a row either vert horiz or diagonally

## create empty board
board = [[' ', ' ',' '],[' ', ' ',' '],[' ', ' ',' ']]
## create index used for player input to enter the square
index = [['1a', '1b', '1c'], ['2a', '2b', '2c'], ['3a', '3b', '3c']]
index2 = [['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3']]
valid_moves = ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c',
'a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']

def draw_board(board):
    print '\n'
    print '     a   b   c'
    print '    -----------'
    print ' 1 | ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' |'
    print '    -----------'
    print ' 2 | ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' |'
    print '    -----------'
    print ' 3 | ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' |'
    print '    -----------'
    return '\n'


## transfer player input to find location on the board
## takes the location input and the index nested list, returns i (for row) and j (for column)
def tfr_loc(loc_in, index, index2):
    for i in range(0, 3):
        for j in range(0, 3):
            if loc_in == index[i][j]:
                return i, j
            elif loc_in == index2[i][j]:
                return i, j
    return 'x', 'x'

## check if space is free - takes row and column info from index and checks if the space is empty
## and therefore free to be moved into
def space_free(i, j):
    return board[i][j] == ' '

## set up a test to see if the winning condition has been met on the board list
def win_cond(board):
    for i in range(0,3):
        ## test for horizontal lines return True if complete
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != ' ':
            return True
        ## test for vertical lines return True if complete
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != ' ':
            return True

    ## check diagonal lines return True if complete
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != ' ':
        return True

    ## If win condition not met, return false
    return False

## procedure that takes input of board and outputs a move based on a set of rules
def comp_opening_move():
    ## go to corners 60% of time
    ## centre 30% and middle 10%
    import random
    start_move = random.randint(1, 10)
    ## if start_move == 1 chose randomly between the 4 side places
    if start_move == 1:
        side_move = random.randint(1, 4)
        if side_move == 1:
            return 'b1'
        if side_move == 2:
            return 'a2'
        if side_move == 3:
            return 'c2'
        if side_move == 4:
            return 'b3'

    ## if start_move is 2, 3, or 4 choose the centre spot
    if start_move > 1 and start_move < 5:
        return 'b2'

    ## if start move == 5 - 10 choose randomly from the corners
    if start_move > 4:
        corner_move = random.randint(1, 4)
        if corner_move == 1:
            return 'a1'
        if corner_move == 2:
            return 'c1'
        if corner_move == 3:
            return 'a3'
        if corner_move == 4:
            return 'c3'

def who_starts():
    print ''
    valid_coin = False
    while valid_coin == False:
        coin_side = raw_input('Do you want (h)eads or (t)ails? ')
        if coin_side == 'h' or coin_side == 't':
            valid_coin = True
        else:
            print "\nyour input is invalid. Try again.\n"
    if coin_side == 'h':
        coin_side_long = "heads"
        coin_side_bin = 0
    if coin_side == 't':
        coin_side_long = "tails"
        coin_side_bin = 1
    print "\nYou chose " + coin_side_long + '\n'
    print 'Getting ready to flip coin\n'
    import time
    time.sleep(1)
    print 'Coin has been flipped\n'
    time.sleep(0.5)
    print 'Coin is in the air, which side will it land on?\n'
    time.sleep(0.5)
    print 'This will determine who starts the game\n'
    time.sleep(0.5)
    print 'OMG\n'
    time.sleep(0.5)
    print 'coin about to land!\n'
    time.sleep(1)
    import random
    coin_flip = random.randint(0, 1)
    if coin_side_bin == coin_flip:
        print "Congratulations its " + coin_side_long + ", you start!\n"
        return True
    if coin_side_bin != coin_flip:
        print "Computer wins coin flip, computer starts!"
        return False

def turn_select(turn, do_you_start):
    if do_you_start == True:
        if turn % 2 == 1:
            player_chip = 'x'
            opp_chip = 'o'
        else:
            player_chip = 'o'
            opp_chip = 'x'
    if do_you_start == False:
        if turn % 2 == 1:
            player_chip = 'o'
            opp_chip = 'x'
        else:
            player_chip = 'x'
            opp_chip = 'o'
    return player_chip, opp_chip

## empty_spaces() takes the board and returns a list of spaces which are empty_spaces
## eg ['a1', 'b3', 'c2'], and the the length of the list
def empty_spaces(board):
    list_of_empty = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == ' ':
                list_of_empty.append(index[i][j])
    return list_of_empty

def comp_random_move(random):
    list_of_empty = empty_spaces(board)
    choose_random_space = random.randint(0, (len(list_of_empty) - 1))
    return list_of_empty[choose_random_space]

## check line by line, if a finishing move is available return True and return the move
def comp_finmove(board, player_chip):
    ## check all horizontal finishing moves avaialble to computer
    for i in range(0, 3):
        line = []
        for j in range(0, 3):
            line.append(board[i][j])
        line_empty = line.count(' ')
        line_player_chip = line.count(player_chip)
        if line_empty == 1 and line_player_chip == 2:
                j = line.index(' ')
                return True, index[i][j]
    ## check all vertical finishing moves avaialble to comp
    for i in range(0, 3):
        line = []
        for j in range(0, 3):
            line.append(board[j][i])
        line_empty = line.count(' ')
        line_player_chip = line.count(player_chip)
        if line_empty == 1 and line_player_chip == 2:
                j = line.index(' ')
                return True, index[j][i]
    ## check diagonal finishing moves avaialble to comp
    ## check line 1a, 2b, 3c
    line = []
    line.append(board[0][0])
    line.append(board[1][1])
    line.append(board[2][2])
    line_empty = line.count(' ')
    line_player_chip = line.count(player_chip)
    if line_empty == 1 and line_player_chip == 2:
            j = line.index(' ')
            return True, index[j][j]

    ## check line 1c, 2b, 3a
    line = []
    line.append(board[0][2])
    line.append(board[1][1])
    line.append(board[2][0])
    line_empty = line.count(' ')
    line_player_chip = line.count(player_chip)
    if line_empty == 1 and line_player_chip == 2:
            j = line.index(' ')
            return True, index[j][2 - j]

    ## if no finishing move avaialble return False and no move
    return False, ' '

## same as comp_finmove() but checks for opponent finishing moves and blocks them
## if a blocking move is avaiable will return "True" and the move
def comp_block_opp_fin(board, opp_chip):
    ## check all horizontal finishing moves avaialble to human
    for i in range(0, 3):
        line = []
        for j in range(0, 3):
            line.append(board[i][j])
        line_empty = line.count(' ')
        line_opp_chip = line.count(opp_chip)
        if line_empty == 1 and line_opp_chip == 2:
                j = line.index(' ')
                return True, index[i][j]
    ## check all vertical finishing moves avaialble to human
    for i in range(0, 3):
        line = []
        for j in range(0, 3):
            line.append(board[j][i])
        line_empty = line.count(' ')
        line_opp_chip = line.count(opp_chip)
        if line_empty == 1 and line_opp_chip == 2:
                j = line.index(' ')
                return True, index[j][i]
    ## check diagonal finishing moves avaialble to comp
    ## check line 1a, 2b, 3c
    line = []
    line.append(board[0][0])
    line.append(board[1][1])
    line.append(board[2][2])
    line_empty = line.count(' ')
    line_opp_chip = line.count(opp_chip)
    if line_empty == 1 and line_opp_chip == 2:
            j = line.index(' ')
            return True, index[j][j]

    ## check line 1c, 2b, 3a
    line = []
    line.append(board[0][2])
    line.append(board[1][1])
    line.append(board[2][0])
    line_empty = line.count(' ')
    line_opp_chip = line.count(opp_chip)
    if line_empty == 1 and line_opp_chip == 2:
            j = line.index(' ')
            return True, index[j][2 - j]

    ## if no finishing move avaialble return False and no move
    return False, ' '

def human_turn(player_chip, index, board, turn, index2):
    ## Displays who's turn it is and requests player move
    print "It is your turn Player: " + player_chip
    loc_in = raw_input("Where would you like to move to? ")
    ## check if user has entered invalid input
    if valid_moves.count(loc_in) == 0:
        print "\nYour input is invalid try again\n"
        return turn
    ## assign i and j using tfr_loc()
    i, j = tfr_loc(loc_in, index, index2)
    ## check if space is free using space_free()
    if space_free(i, j) == True:
        ## update board to include new move
        board[i][j] = player_chip
        ## displays board with new move
        print draw_board(board)
        ## test if win condition met after the latest move - If met declear winner
        if win_cond(board) == True:
            print "Congratulations Player " + player_chip + " - You Win!!!"
            turn = -1
            return turn
        ## turn count increases to next turn
        turn = turn + 1
    else:
        print "\nThe space you have selected is occupied"
        print draw_board(board)
    return turn

def comp_turn(player_chip, opp_chip, index, board, turn, random, time, index2):
    print 'It is computers turn'
    can_comp_fin, comp_fin_moveref = comp_finmove(board, player_chip)
    can_comp_block, comp_block_moveref = comp_block_opp_fin(board, opp_chip)
    if len(empty_spaces(board)) == 9:
        comp_move = comp_opening_move()
    elif can_comp_fin == True:
        comp_move = comp_fin_moveref
    elif can_comp_block == True:
        comp_move = comp_block_moveref
    else:
        comp_move = comp_random_move(random)
    time.sleep(1)
    print 'Computer decides to take space ' + comp_move
    ## assign i and j using tfr_loc()
    i, j = tfr_loc(comp_move, index, index2)
    ## update the board to reflect the computers move
    board[i][j] = player_chip
    ## displays board with new move
    print draw_board(board)
    ## test if win condition met after the latest move - If met declear winner
    if win_cond(board) == True:
        print "You lose, computer is victorious!"
        turn = -1
        return turn
    ## turn count increases to next turn
    turn = turn + 1
    return turn

## plays the game vs the computer
def vs_comp():
    import time
    import random

    print "\ncomputer is the 'x' and you are the 'o'"
    print "we will flip a coin to see who starts"
    do_you_start = who_starts()
    ## print empty board
    print draw_board(board)
    ## initialise turn to 0
    turn = 0
    while turn < 9:
        ## determines the correct player chip and opponent chip for the turn
        player_chip, opp_chip = turn_select(turn, do_you_start)
        ## runs through what happens for each human turn
        if player_chip == 'o':
            turn = human_turn(player_chip, index, board, turn, index2)
        ## runs through computers turn
        if player_chip == 'x':
            turn = comp_turn(player_chip, opp_chip, index, board, turn, random, time, index2)
        ## ends procedure if game has been won
        if turn == -1:
            return "\nPlay again soon!"
        ## If all board filled up display draw message
        if turn == 9:
            return "This game is a draw.\n\nPlay again soon!"
    return

## two_player_game() runs the game until it is won lost or drawn
def two_player_game():
    ## set initial turn to be turn 0
    turn = 0
    ## print blank board
    print draw_board(board)
    ## while loop runs until board is full and game is drawn
    while turn < 9:
        ## Determines who's turn is
        if turn % 2 == 1:
            player_chip = 'x'
        else:
            player_chip = 'o'
        turn = human_turn(player_chip, index, board, turn, index2)
        ## exit procedure if game has ended
        if turn == -1:
            return
        ## If all board filled up display draw message
        if turn == 9:
            print "This game is a draw."
    return

print vs_comp()
## print comp_opening_move()
