
def show(board):
    for row in board:
        print("".join(row))

    print()


def main():

    total = 0
    board = []
    lines = []
    with open("day4/input.txt","r") as file:
        lines = file.readlines()
        for line in lines:

            board.append(list(line.strip()))

    # show(board)
    width = len(board[0])
    height = len(board) 

    finish = False
    temp = []
    for i in board:
        temp.append(i[:])


    while not finish:
        # show(board)

        updated = 0

        for row in range(width):
            for col in range(height):
                neighbours = 0
                if board[row][col] != "@":
                    continue
                if col > 0 and board[row][col-1] == "@":
                    neighbours += 1
                if col < width-1 and board[row][col+1] == "@":
                    neighbours += 1
                if row > 0 and board[row-1][col] == "@":
                    neighbours += 1
                if row < height-1 and board[row+1][col] == "@":
                    neighbours += 1
                if col > 0 and row > 0 and board[row-1][col-1] == "@":
                    neighbours += 1
                if col > 0 and row < height-1 and board[row+1][col-1] == "@":
                    neighbours += 1
                if col < width-1 and row > 0 and board[row-1][col+1] == "@":
                    neighbours += 1
                if col < width-1 and row < height-1 and board[row+1][col+1] == "@":
                    neighbours += 1
                # print(neighbours)
                if neighbours < 4 :
                    temp[row][col] = "x"
                    updated += 1
                    total += 1

        # finish = True
        if updated == 0:
            finish = True

        board = []
        for i in temp:
            board.append(i[:])
    # show(temp)
    print(total)

if __name__ == "__main__":
    main()