def main():
    # Your code goes here

    #initialise
    def initialiseBoard():
        print("   1 2 3")
        
        for i in range(3):
            row = ['-','-','-']
            board.append(row)

    #Display
    def displayBoard():
          
        x = 0
        for i in board:
            if x == 0:
                letter = 'A'

            if x == 1:
                letter = 'B'
                
            if x == 2:
                letter = 'C' 
            x = (x + 1)
            print(letter,'|', end = '')
            for column in i:
                print(column, end = '|')
            print()

    #WinChecks
    def checkdiagonal():
        if board[0][0] == board[1][1] == board[2][2]:
            return True
        
        if board[0][2] == board[1][1] == board[2][0]:
            return True
        return False

    #def checkvertical():
    

    board = []
    playercount = 1
    initialiseBoard()
    displayBoard()

    #Selecting
    
    while True:


        token = "X"
        player = "X"
        if playercount % 2 == 0:
            token = "O"
            player = "O"

        print()
        choice = int(input(f"{player}, Select a spot:"))
        
        print()
        choice -= 1

        for i in range(2, -1, -1):
                if board[i][choice] == '-':
                    board[i][choice] = token
                    playercount += 1
                    break

        displayBoard()
        checkdiagonal()   

    print(f"{player} is the winner!")

if __name__ == "__main__":
    main()

       