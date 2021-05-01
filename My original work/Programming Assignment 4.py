import nltk # Must use nltk data as well!!!!!
import string
# This section is for extracting words from a file and
# creats a bigrm for the entire file
# cwd is /home/derek/Downloads

with open("shakespear.txt", "r") as f:
    text = f.read()



data = nltk.word_tokenize(text)
bigrmList = list(nltk.bigrams(data))

# This section is for taking the bigrm and counting the
# amount of times they repeat
countDic = {}
for bigrm in bigrmList:
    if bigrm in countDic:
        countDic[bigrm] = countDic[bigrm] + 1
    else:
        countDic[bigrm] = 1


f = open("bigrm-results.txt", "w")
for result, count in countDic:
    work = result
    work2 = count
    f.write(work)
    f.write(",")
    f.write(work2)
    f.write("\n")
f.close()

# Calculating frequency
f = open("bigrm-results.txt", "r")
freqDir = {}
for line in f:
    placeHol = line
    if placeHol in freqDir:
        freqDir[line] = freqDir[line] + 1
    else:
        freqDir[line] = 1
f.close()


# sort the dictionary
sortedDir = {k: v for k, v in sorted(freqDir.items(), key=lambda item: item[1])}

# print the output
f = open("bigrm-results.txt", "w")
for bigrm, count in list(sortedDir.items()):
    # (a, b) = bigrm
    f.write(bigrm + " " + str(count) + "\n")

f.close()
