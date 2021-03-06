## playable backgammon

## create the structure of the board a list of 24 elements, each element contains a list of 2 elements
## the first is either ' ' (empty space), 'B' (black occupied) or 'W' (white occupied)
## the second is either ' ' (if empty, or a number representing how many pieces are on the space)

board = [[' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '],
 [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '],
  [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '],
   [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' ']]

## updates board to show starting position
board = [['B', 2], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], ['W', 5],
 [' ', ' '], ['W', 3], [' ', ' '], [' ', ' '], [' ', ' '], ['B', 5],
  ['W', 5], [' ', ' '], [' ', ' '], [' ', ' '], ['B', 3], [' ', ' '],
   ['B', 5], [' ', ' '], [' ', ' '], [' ', ' '], [' ', ' '], ['W', 2]]

jail = [['B', 0], ['W', 0]]
offboard = [['B', 0], ['W', 0]]

def draw_board(board):

    print '\n ---------------------------------------------------------------------------------------'
    print ' |\  ' + board[0][0] + '  /\  ' + board[1][0] + '  /\  ' + board[2][0] + '  /\  ' + \
    board[3][0] + '  /\  ' + board[4][0] + '  /\  ' + board[5][0] + '  /|\  ' + \
    board[6][0] + '  /\  ' + board[7][0] + '  /\  ' + board[8][0] + '  /\  ' + \
    board[9][0] + '  /\  ' + board[10][0] + '  /\  ' + board[11][0] + '  /| '
    print ' | \ ' + str(board[0][1]) + ' /  \ ' + str(board[1][1]) + ' /  \ ' + str(board[2][1]) + ' /  \ ' + \
    str(board[3][1]) + ' /  \ ' + str(board[4][1]) + ' /  \ ' + str(board[5][1]) + ' / | \ ' + \
    str(board[6][1]) + ' /  \ ' + str(board[7][1]) + ' /  \ ' + str(board[8][1]) + ' /  \ ' + \
    str(board[9][1]) + ' /  \ ' + str(board[10][1]) + ' /  \ ' + str(board[11][1]) + ' / | '
    print ' |  \ /    \ /    \ /    \ /    \ /    \ /  |  \ /    \ /    \ /    \ /    \ /    \ /  |'
    print ' |                                          |                                          |'
    print ' |                                          |                                          |'
    print ' |                                          |                                          |'
    print ' |  / \    / \    / \    / \    / \    / \  |  / \    / \    / \    / \    / \    / \  |'
    print ' | / ' + str(board[23][1]) + ' \  / ' + str(board[22][1]) + ' \  / ' + str(board[21][1]) + ' \  / ' + \
    str(board[20][1]) + ' \  / ' + str(board[19][1]) + ' \  / ' + str(board[18][1]) + ' \ | / ' + \
    str(board[17][1]) + ' \  / ' + str(board[16][1]) + ' \  / ' + str(board[15][1]) + ' \  / ' + \
    str(board[14][1]) + ' \  / ' + str(board[13][1]) + ' \  / ' + str(board[12][1]) + ' \ | '
    print ' |/  ' + board[23][0] + '  \/  ' + board[22][0] + '  \/  ' + board[21][0] + '  \/  ' + \
    board[20][0] + '  \/  ' + board[19][0] + '  \/  ' + board[18][0] + '  \|/  ' + \
    board[17][0] + '  \/  ' + board[16][0] + '  \/  ' + board[15][0] + '  \/  ' + \
    board[14][0] + '  \/  ' + board[13][0] + '  \/  ' + board[12][0] + '  \| '
    print ' ---------------------------------------------------------------------------------------\n'
    print 'Black has: ' + str(jail[0][1]) + ' pieces in jail, and ' + str(offboard[0][1]) + ' pieces off the board\n'
    print 'White has: ' + str(jail[1][1]) + ' pieces in jail, and ' + str(offboard[1][1]) + ' pieces off the board\n'

print draw_board(board)
