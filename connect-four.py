
    # Your code goes here
board = []
#inializing board

def initialiseBoard():
    for i in range(6):
        row = ['-','-','-','-','-','-','-']
        board.append(row)
    

#displaying board
def displayBoard():
    for i in board:
        for column in i:
            print(column, end = '|')
        print()

initialiseBoard()
displayBoard()
playercount = 1

#selection

while True:

    token = "X"
    if playercount % 2 == 0:
        token = "O"
    playercount += 1


    choice = int(input("Select a column:"))
    choice -= 1

    for i in range(5, -1, -1):
       
        board[5][choice] = token
    displayBoard()

        








