def main():
    code = 0
    num = 50
    with open("input.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            if line[0] == "R":
                line = line[1:]
                num += int(line)
            else:
                line = line[1:]
                num -= int(line)

            num = num% 100
            if num == 0:
                code += 1

    print(code)
    pass


if __name__ == "__main__":
    main()