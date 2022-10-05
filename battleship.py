import random
import os

# Dimensions of our Board and ship size constant
SHIP_SIZE = 4
DIMENSION = 10
L = 0 # for printing Alphabets above our board
board = []

# creating board
for row in range(DIMENSION):
    row_list = []
    for col in range(DIMENSION):
        row_list.append(' ')
    board.append(row_list)


#random selection of row and column for our ship
#selction of orientation according to available space
col_ship = random.randint(0,DIMENSION-1)
#when column of ship is greater than 6 we need to change the orientation
if col_ship > 6:
    row_ship = random.randint(0,6)
    orien = 0  # orientaton would be downwards
else:
    row_ship = random.randint(0,9)
    if row_ship > 6:
        orien = 1 #orientation would be right side
    else:
        orien = random.randint(0,1)

#we will create another board list, so that to check wheather player hit the ship by comparing the board's lists
#we will not print this second board.
board1 = []
for row in range(DIMENSION):
	row_list1=[]
	for col in range(DIMENSION):
		row_list1.append(" ")
	board1.append(row_list1)


#now placing our ship into the board at random position

board1[row_ship][col_ship] = "&"
if orien == 1:
    for i in range(SHIP_SIZE-1):
        col_ship = col_ship+1
        board1[row_ship][col_ship] = "&"
else:
    for i in range(SHIP_SIZE-1):
        row_ship = row_ship+1
        board1[row_ship][col_ship] = "&"

#now we need to print our first board for player as display screen
for cols in range(DIMENSION): 
    print('   ' + chr(65+L), end='')
    L = L+1

print("\n +" + "---+" * DIMENSION)
for row in range(DIMENSION):
    print(str(row) + '|', end=' ')
    for col in range(DIMENSION):
        print(board[row][col] + ' | ', end='')

    print("\n +"+"---+"*DIMENSION)

# Asking for input from player
SCORE = 0
NO_HIT = 0

while NO_HIT < 4:
    players_input = list(input("Sergeant enter the coordinates of the ship in the form of 'A7' to hit it: "))
    print("Roger That")
    guess_col = ord(players_input[0]) - 65
    guess_row = int(players_input[1])
    while str(players_input[1]).isdigit() != True or guess_col < 0 or guess_col >9:
        players_input = list(input("Sergeant Wrong format enter the coordinates again to hit the ship: "))
        print("Roger That")
        guess_col = ord(players_input[0]) - 65
        guess_row = int(players_input[1])
    
    # checking for hit
    
    if board1[guess_row][guess_col] == "&":
        NO_HIT = NO_HIT+1
        SCORE = SCORE+10
        board[guess_row][guess_col] = "X"

        os.system("clear")
        # os.system('cls')
        # print the board again to see what happen to the ship
        for cols in range(DIMENSION):
            col_No = chr(cols+65) 
            print('   ' + col_No, end='')
            
        print("\n +" + "---+" * DIMENSION)
        for row in range(DIMENSION):
            print(str(row) + '|', end=' ')
            for col in range(DIMENSION):
                print(board[row][col] + ' | ', end='')

            print("\n +"+"---+"*DIMENSION)

    else:
        board[guess_row][guess_col] = "#"
        os.system("clear")
        # os.system('cls')

        for cols in range(DIMENSION):
            col_No = chr(cols+65) 
            print('   ' + col_No, end='')
            
        print("\n +" + "---+" * DIMENSION)
        for row in range(DIMENSION):
            print(str(row) + '|', end=' ')
            for col in range(DIMENSION):
                print(board[row][col] + ' | ', end='')

            print("\n +"+"---+"*DIMENSION)

# Printing Score 
print("Game over! the ship is sunk" + str(SCORE) + "Thankyou for playing")




