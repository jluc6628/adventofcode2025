def main():
    lines = ""
    total = 0
    with open("day3/input.txt","r") as file:
        lines = file.readlines()

        for line in lines:
            if line[-1] == "\n":
                line = line[:len(line) -1]
            length = len(line)
            entry = [int(num) for num in line]


            num = ""
            for i in range(11,0,-1):
                
                max_i = 0
                digit = -1
                temp = entry.copy()
                temp = temp[:-i]

                for j in range(len(temp)):
                    if temp[j] > digit:
                        digit = temp[j]
                        max_i = j
                num += str(digit)

                entry = entry[max_i+1:]

            num += str(max(entry))
            

            total += int(num)
                 
    print(total)


if __name__ == "__main__":
    main()

