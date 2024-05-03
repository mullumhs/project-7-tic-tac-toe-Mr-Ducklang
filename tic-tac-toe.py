def main():
    # Your code goes here

    #initialise
    def initialiseBoard():
        
        
        for i in range(3):
            row = ['-','-','-']
            board.append(row)

    #Display
    def displayBoard():
        print()
        print("=== TIC TAC TOE===")
        print()
        print("   1 2 3")
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

    #WinCheck
    def checkwin(): 
        #first number is down. second is across
    
        #across top
        if board[0][0] == board[0][1] == board[0][2] and board[0][1] != '-':
            return True
        #down left
        if board[0][0] == board[1][0] == board[2][0] and board[1][0] != '-':
            return True
        #diagonal 1
        if board[0][0] == board[1][1] == board[2][2] and board[1][1] != '-':
            return True
        #down middle
        if board[0][1] == board[1][1] == board[2][1] and board[1][1] != '-':
            return True
        #across middle
        if board[1][0] == board[1][1] == board[1][2] and board[1][1] != '-':
            return True
        #down right
        if board[0][2] == board[1][2] == board[2][2] and board[1][2] != '-':
            return True
        #across bottom
        if board[2][0] == board[2][1] == board[2][2] and board[2][1] != '-':
           return True
        #diagonal 2
        if board[0][2] == board[1][1] == board[2][0] and board[1][1] != '-':
            return True
        return False

    #Draw Check
    def CheckDraw():

        for row in board:

            for cell in row:

                if cell == '-':

                    return False

        return True

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
        choice = input(f"{player}, Select a column (number): ")
        choice2 = input("Select a row (letter): ")

        print()
        choice -= 1

    
        if board[choice2][choice] == '-':
            board[choice2][choice] = token
            playercount += 1
            break

        displayBoard()
        if checkwin():
            print()
            print(f'{player} Wins!')
            break
        if CheckDraw():
            print()
            print(f'Draw! No Winners!')
            break  

        

    

if __name__ == "__main__":
    main()

print()
Answer = input("Enter any key to start the next game: ") 

main()