import argparse
with open("/Users/hailongwang/git/chris/data_analysis/annoted_myDiff50p.csv") as f:
    line = f.readline()
    print(line)
    namesFound = []
    indexes = []
    count = 1
    while line:
        line = f.readline()
        arr = line.split(",")
        print(arr)
        if len(arr) > 1:
            if arr[2] not in namesFound:
                namesFound.append(arr[2])
                indexes.append(count)
            count += 1
    print(indexes)
    with open("/Users/hailongwang/git/chris/data_analysis/entries.txt", "w") as f:
        f.write("\n".join(namesFound))
