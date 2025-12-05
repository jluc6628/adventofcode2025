def main():
    ranges = []
    ingredients = []
    total = 0
    with open("day5/input.txt","r") as file:
        lines = file.readlines()
        first = True
        for line in lines:
            line = line.strip("\n")
            
            if line == "":
                first = False
                continue

            if first:
                ranges.append([int(x) for x in line.split("-")])
            else:
                ingredients.append(int(line))
    for i in ingredients:
        spoil = True
        for low, high in ranges:
            if low <= i <= high:
                spoil = False
                total += 1
                # print(low,high,i)
                break


    print(total)
            


if __name__ == "__main__":
    main()