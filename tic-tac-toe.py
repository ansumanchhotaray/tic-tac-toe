grid = ["1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]

print("Tic-tac-toe")
print("Use the following numbers for positions in the grid:")
for row in range(3):
    for column in range(3):
        print(grid[3 * row + column], end=" ")
    print()

filled = 0
win = False

while filled < 9:
    # Player 1
    x = int(input("Player 1: "))

    while grid[x - 1] == "x" or grid[x - 1] == "o":
        print("Already filled. Try again!")
        x = int(input("Player 1: "))

    grid[x - 1] = "x"

    for row in range(3):
        for column in range(3):
            print(grid[3 * row + column], end=" ")
        print()

    for row in range(3):
        if grid[3 * row] == "x" and grid[3 * row + 1] == "x" and grid[3 * row + 2] == "x":
            win = True

    for column in range(3):
        if grid[column] == "x" and grid[column + 3] == "x" and grid[column + 6] == "x":
            win = True

    if grid[0] == "x" and grid[4] == "x" and grid[8] == "x":
        win = True

    if grid[2] == "x" and grid[4] == "x" and grid[6] == "x":
        win = True

    if win == True:
        print("Player 1 wins!")
        break

    filled += 1

    # Draw condition
    if filled == 9:
        print("Draw!")
        break

    # Player 2
    o = int(input("Player 2: "))

    while grid[o - 1] == "x" or grid[o - 1] == "o":
        print("Already filled. Try again!")
        o = int(input("Player 2: "))

    grid[o - 1] = "o"

    for row in range(3):
        for column in range(3):
            print(grid[3 * row + column], end=" ")
        print()

    for row in range(3):
        if grid[3 * row] == "o" and grid[3 * row + 1] == "o" and grid[3 * row + 2] == "o":
            win = True
            break

    for column in range(3):
        if grid[column] == "o" and grid[column + 3] == "o" and grid[column + 6] == "o":
            win = True
            break

    if grid[0] == "o" and grid[4] == "o" and grid[8] == "o":
        win = True

    if grid[2] == "o" and grid[4] == "o" and grid[6] == "o":
        win = True

    if win == True:
        print("Player 2 wins!")
        break

    filled += 1
