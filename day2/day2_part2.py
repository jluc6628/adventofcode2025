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

            multiples = []
            for j in range(1,len(entry)):
                if (len(entry)% j == 0):
                    multiples.append(j)

            for j in multiples:
                slice = entry[:j]

                if all(x == "" for x in entry.split(slice)):

                    total += i
                    break



    print(total)




if __name__ == "__main__":
    main()