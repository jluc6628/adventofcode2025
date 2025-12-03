def main():

    total = 0
    input = []
    
    with open("day2/input.txt","r") as file:

        line = file.read()
        input = line.split(",")

    for entry in input:
        start,end = entry.split("-")
        
        for i in range(int(start),int(end)+1):

            entry = str(i)
            if len(entry) % 2 == 1:
                continue

            half = int( len(entry) / 2)
            if entry[:half] == entry[half:]:
                total += i



    print(total)








if __name__ == "__main__":
    main()