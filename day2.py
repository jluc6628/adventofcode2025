def main():
    code = 0
    current = 50

    with open("input.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            neg = False
            if line[0] == "R":
                line = line[1:]
                num = int(line)
            else:
                neg = True
                line = line[1:]
                num = -int(line)

            if num >0:
                while(num >0):
                    current += 1
                    if current % 100 == 0:
                        code +=1
                    num -= 1

            else:
                while(num<0):
                    current -= 1
                    if current % 100 == 0:
                        code += 1
                    num += 1







            # current = current% 100
            # if current == 0:
            #     code += 1

            # print("step", current,"code", code)
            # print()

    print(code)
    pass


if __name__ == "__main__":
    main()