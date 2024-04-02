
    # Your code goes here

#main
def main():
    board = initialiseBoard()
    displayBoard(board)
    currentplayer = 1
   

#initialise/create board
def initialiseBoard():
    board = []
    for _ in range(6):
        row = []
        for _ in range(7):
            row.append('-')
        board.append(row)
    return board
    
#display board
def displayBoard(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()
    print()
    
main()