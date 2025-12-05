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


    fresh = []

    ranges = sorted(ranges)

    for low, high in ranges:
        if len(fresh) == 0 or fresh[-1][1] < low:
            fresh.append([low, high])
        else:
            fresh[-1][1] = max(fresh[-1][1], high)
    # print(fresh)

    for low,high in fresh:
        total += high-low + 1
    print(total)
            


if __name__ == "__main__":
    main()