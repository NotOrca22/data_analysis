text = []
with open("/Users/hailongwang/git/chris/data_analysis/annoted_myDiff50p.csv") as file:
    line = "orca"
    while line:
        line = file.readline()
        if line:
            text.append(line.split(" "))
with open("/Users/hailongwang/git/chris/data_analysis/entries_1.txt") as f:
    line = "orca" # to make sure line == True
    while line:
        line = f.readline()
        if line:
            splitLine = line.split("\t")
            for line in text:
                if len(splitLine) > 1:
                    if len(line) > 2:
                        if line[2] == splitLine[0]:
                            line[3] = splitLine[1]
                    else:
                        break
                else:
                    break

with open("/Users/hailongwang/git/chris/data_analysis/result.txt", "w") as f:
    for line in text:
        f.write("\t".join(line))