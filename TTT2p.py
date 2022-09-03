#board array
board = [ ["1","2","3"], 
          ["4","5","6"], 
          ["7","8","9"] ]

#functions

#prints the board
def printBoard():
    print("   Board   ")
    for y in range(3):
        print(" ", end = "")
        for x in range(2):
            print(board[y][x], end = " | ")
        print(board[y][x + 1])
        if y<2:
            print("-----------")

#function for a single play
def play(i):
    s=input("Play: ")
    while not isI(s) or occupied(int(s)):
        if not isI(s):
            s=input("Choose a number from the coordinate system (1-9) ")
        else:
            s=input("Play in a non-occupied area ")
    if i % 2 == 0:
        board[ convert(int(s))[0] ][ convert(int(s))[1] ] = "X"
    else:
        board[ convert(int(s))[0] ][ convert(int(s))[1] ] = "O"

#returns if the string is an int
def isI(s:str) -> bool:
    for c in s:
        if 48 < ord(c) < 58:
            return True
    return False

#converts the single digit input to the 2 digit coordinate
def convert(i:int) -> list:
    return [(i-1)//3,(i-1)%3]

#returns if the space is occupied
def occupied(i:int) -> bool:
    return board[ convert(i)[0] ][ convert(i)[1] ] != " "

#returns winner
    #0 - none
    #1 - X
    #2 - O
def win() -> int:
    for x in range(3):
        if board[0][x] == board[1][x] == board[2][x]:
            if board[0][x] == "X":
                return 1
            if board[0][x] == "O":
                return 2
    for y in range(3):
        if board[y][0] == board[y][1] == board[y][2]:
            if board[y][0] == "X":
                return 1
            if board[y][0] == "O":
                return 2
    if board[0][0] == board[1][1] == board[2][2]:
        if board[1][1] == "X":
            return 1
        if board[1][1] == "O":
            return 2
    if board[2][0] == board[1][1] == board[0][2]:
        if board[1][1] == "X":
            return 1
        if board[1][1] == "O":
            return 2
    return 0


#script

printBoard()
for y in range(3):
    for x in range(3):
        board[y][x] = " "
for i in range(9):
    play(i)
    printBoard()
    if win() == 1:
        print("X wins!")
        break
    if win() == 2:
        print("O wins!")
        break
if win() == 0:
    print("Tie!")
