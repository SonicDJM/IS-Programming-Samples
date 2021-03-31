
def searchFunct(source, query):

    if query in source.keys():
        return source[query]
    else:
        return []



def main():
    fileDict = {}

    f = open("/home/derek/rando_graph.tsv", 'r')
    for line in f:

        key, value = line.split("\t")
        value = value.strip("\n")
            
        if key in fileDict.keys():
            fileDict[key].append(value)

        else:
            fileDict[key] = [value]
    f.close()
    while True:
        searchKey = str(input("Please type in a number from 1 to 6474, type 'exit' to leave: "))
        if searchKey == "exit":
            break
        searchKey = int(searchKey)
        if searchKey in range(1, 6474 + 1):
            print(f'The number is connected to: {searchFunct(fileDict, str(searchKey))}')
        else:
            print("Out of range, please try again")


if __name__ == "__main__":
    main()
