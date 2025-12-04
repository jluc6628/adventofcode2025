def main():

    total = 0
    with open("day3/input.txt","r") as file:
        lines = file.readlines()

        for line in lines:
            if line[-1] == "\n":
                line = line[:len(line) -1]
            length = len(line)
            entry = [int(num) for num in line]


            second = -1
            first = -1

            temp = entry.copy()
            end =temp.pop()
            max_i = 0
            for i in range(len(temp)):
                if temp[i] > first:
                    first = temp[i]
                    max_i = i

            temp.pop(max_i)

            temp = temp[max_i:]
            temp.append(end)

            for i in range(len(temp)):
                if temp[i] > second:
                    second = temp[i]

            num = int(str(first) + str(second))

            total += num
                 
    print(total)


if __name__ == "__main__":
    main()