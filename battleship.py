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
#selection of orientation according to available space
col_ship = random.randint(0,DIMENSION-1)
#when column of ship is greater than 6 we need to change the orientation
if col_ship > 6:
    row_ship = random.randint(0,6)
    orien = 0  # orientation would be downwards
else:
    row_ship = random.randint(0,9)
    if row_ship > 6:
        orien = 1 #orientation would be right side
    else:
        orien = random.randint(0,1)

#we will create another board list, so that to check weather player hit the ship by comparing the board's lists
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
    # if our input is over one digit last no. for ex = 13, 15, 10 etc
    # if our input is less than 2 then assign it -1 so that it get process in next while loop to get valid input to process

    if len(players_input) >= 3 and players_input[1].isdigit() and players_input[2].isdigit():
        temp_guess_row = (players_input[1]+players_input[2])
        check_guess_row = int(temp_guess_row)
        check_guess_col = (ord(players_input[0])-65)
    elif len(players_input) == 2 and players_input[1].isdigit():
        temp_guess_row = (players_input[1])
        check_guess_row = int(temp_guess_row)
        check_guess_col = (ord(players_input[0])-65)
    else:
        temp_guess_col = -1
        temp_guess_row = -1
        check_guess_row = int(temp_guess_row)
        check_guess_col = int(temp_guess_col)

    # checking for valid input
    # weather first first element of our Alphabet or not and second element is a no. or not
    # then checking for the range of our input, weather its a within the scope of board or not
    # if length of input is less than 1 or o then ask for input again
    while (len(players_input) <= 1 or players_input[0].isdigit()) == True or (players_input[1].isdigit()) == False or\
            ord(players_input[0])-65 > DIMENSION or ord(players_input[0])-65 < 0 or int(temp_guess_row) > DIMENSION\
            or check_guess_col < 0 or check_guess_col >= DIMENSION\
        or check_guess_row < 0 or check_guess_row >= DIMENSION or int(temp_guess_row) < 0 or board[check_guess_row][check_guess_col] == "X"\
    or board[check_guess_row][check_guess_col] == "O":
        players_input = list(input(
            "Please enter the coordinates again in correct format like A6, B2, C9 etc. and within the range : "))

        # here we are checking our input weather its within range of valid inputs like only A is invalid if A13 then then separating "A" and "13"
        # and checking our third digit of input is a number or not like A3A is invalid so need the input again
        if len(players_input) >= 3 and players_input[1].isdigit() and players_input[2].isdigit():
            temp_guess_row = (players_input[1]+players_input[2])
            check_guess_row = int(temp_guess_row)
            check_guess_col = (ord(players_input[0])-65)
        elif len(players_input) == 2 and players_input[1].isdigit():
            temp_guess_row = (players_input[1])
            check_guess_row = int(temp_guess_row)
            check_guess_col = (ord(players_input[0])-65)
        else:
            temp_guess_col = -1
            temp_guess_row = -1
            check_guess_row = int(temp_guess_row)
            check_guess_col = int(temp_guess_col)
        # print(check_guess_col, check_guess_row)

    # now this condition help to process higher digit inputs like A11 or A54
    if len(players_input) >= 3:
        comb_no = players_input[1]+players_input[2]
        guess_row = int(comb_no)
    else:
        guess_row = int(players_input[1])

    guess_col = (ord(players_input[0])-65)
    
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
        SCORE = SCORE-5
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
print("Game over! the ship is sunk and the score is: " + str(SCORE) + " Thankyou for playing")




