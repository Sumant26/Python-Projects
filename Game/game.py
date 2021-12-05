puzzle = [
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 1]
]

position = [0, 0]

RED = '\033[91m'
END = '\033[0m'
GREEN = '\033[92m'


print("\n\n\nInstructions:")
print("W - to go up")  
print("S - to go down")
print("A - to go left")
print("D - to go right")
print("0 is the wall(obstacle)")
print("1 is the path")

print("\n\n\nHERE IS THE MATRIX:\n\n\n")

#enumerate
def printPuzzle():
    for rIndex, row in enumerate(puzzle):
        for cIndex, column in enumerate(row):
            if position[0] == rIndex and position[1] == cIndex:
                print("*", end=" ")
            else:
                print(f"{column}", end=" ")
        print("")

printPuzzle()
choice = ''

while(choice != 'E'):
    print("Please enter your input \n")
    choice = input()

    if choice == 'S' or choice == 's':
        nextPostion = puzzle [position[0] + 1] [position[1]]
        if position[0] == len(puzzle) - 1 or nextPostion == 0:
            print(f"{RED}INVALID POSITION{END}")
        else:
            position[0] = position[0] + 1
    if choice == 'W' or choice == 'w':
        nextPostion = puzzle [position[0] - 1][position[1]]
        if position[0] == 0 or nextPostion == 0:
            print(f"{RED}INVALID POSITION{END}")
        else:
            position[0] = position[0] - 1
    if choice == 'A' or choice == 'a':
        nextPostion = puzzle[position[0]][position[1] - 1]
        if position[1] == 0 or nextPostion == 0:
            print(f"{RED}INVALID POSITION{END}")
        else:
            position[1] = position[1] - 1
    if choice == 'D' or choice == 'd': 
        if position[1] == len(puzzle[0]) - 1:
            print(f"{RED}INVALID POSITION{END}")
        elif puzzle[position[0]][position[1] + 1] == 0:
            print(f"{RED}INVALID POSITION{END}")
        else:
            position[1] = position[1] + 1
    
    
    printPuzzle()
    if position[0] == len(puzzle) - 1 and position[1] == len(puzzle[0]) - 1:
        print(f"{GREEN}YOU WON!!{END}")
        break