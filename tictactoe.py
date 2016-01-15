## The game tic tac toe where you win by getting 3 of your pieces
## in a row either vert horiz or diagonally

## create empty board
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
## create index used for player input to enter the square
index = [['a1', 'b1', 'c1'], ['a2', 'b2', 'c2'], ['a3', 'b3', 'c3']]

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
    print '\n'
    return

## transfer player input to find location on the board
## takes the location input and the index nested list, returns i (for row) and j (for column)
def tfr_loc(loc_in, index):
    for i in range(0, 3):
        for j in range(0, 3):
            if loc_in == index[i][j]:
                return i, j
    return 'x', 'x'

## check if space is free - takes row and column info from index and checks if the space is empty
## and therefore free to be moved into
def space_free(i, j):
    if board[i][j] == ' ':
        return True
    else:
        return False

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

## gameflow() runs the game until it is won lost or drawn
def gameflow():
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

        ## Displays who's turn it is and requests player move
        print "Player: " + player_chip
        loc_in = raw_input("Where would you like to move to? ")

        ## assign i and j using tfr_loc()
        i, j = tfr_loc(loc_in, index)

        ## check if space is free using space_free()
        if space_free(i, j) == True:
            ## update board to include new move
            board[i][j] = player_chip
            ## displays board with new move
            print draw_board(board)
            ## test if win condition met after the latest move - If met declear winner
            if win_cond(board) == True:
                print "Congratulations Player " + player_chip + " - You Win!!!"
                return
            ## turn count increases to next turn
            turn = turn + 1
        else:
            print "The space you have selected is either invalid or not occupied"
            print draw_board(board)

        ## If all board filled up display draw message
        if turn == 9:
            print "This game is a draw."
    return

print gameflow()
