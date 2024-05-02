
    # Your code goes here

#inializing board

def initialiseBoard():
    print("1 2 3 4 5 6 7")
    print()
    for i in range(6):
        row = ['-','-','-','-','-','-','-']
        board.append(row)
    


#displaying board
def displayBoard():
    for i in board:
        print('|', end = '')
        for column in i:
            print(column, end = '|')
        print()

def checkhorizontal():
    for row in range(6):
        for column in range(4):
            if (board[row][column] == board[row][column + 1] ==
                board[row][column + 2] == board[row][column + 3] != '-'):
                  return True
        return False


board = []
playercount = 1

initialiseBoard()
displayBoard()


#selection

while True:
    

    token = "X"
    player = "Player 1"
    if playercount % 2 == 0:
        token = "O"
        player = "Player 2 "
    

    
    choice = int(input(f"{player}, Select a column:"))
    print()
    choice -= 1

    for i in range(5, -1, -1):
        if board[i][choice] == '-':
            board[i][choice] = token
            playercount += 1
            break


    displayBoard()
    checkhorizontal()

        
print(f"Congrats {player}! You Win")







