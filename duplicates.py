import argparse
def removeDuplicates(input_file):
    with open(input_file) as f:
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
        # with open(output_file, "w") as f:
        #     f.write("\n".join(namesFound))

def replaceGenes(input_file, gene_file, result_file):
    text = []
    with open(input_file) as file:
        line = "orca"
        while line:
            line = file.readline()
            if line:
                text.append(line.split(" "))
    with open(gene_file) as f:
        line = "orca"  # to make sure line == True
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

    with open(result_file, "w") as f:
        for line in text:
            f.write("\t".join(line))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", help="add the input file", action="store", dest="input_file")
    # parser.add_argument("--output_file", help="add the output file", action="store", dest="output_file")
    parser.add_argument("--gene_file", help="add the gene file", action="store", dest="gene_file")
    parser.add_argument("--result_file", help="add the result file", action="store", dest="result_file")
    args = parser.parse_args()
    removeDuplicates(args.input_file)
    replaceGenes(args.input_file, args.gene_file, args.result_file)