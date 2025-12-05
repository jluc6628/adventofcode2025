
def show(board):
    for row in board:
        print("".join(row))

    print()

def main():

    total = 0
    board = []
    lines = []
    with open("day4/input1.txt","r") as file:
        lines = file.readlines()
        for line in lines:

            board.append(list(line.strip()))

    width = len(board[0])
    height = len(board) 

    temp = []
    for i in board:
        temp.append(i[:])

    show(board)



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
            if neighbours < 4 :
                temp[row][col] = "x"
                total += 1

    show(temp)
    print(total)

if __name__ == "__main__":
    main()