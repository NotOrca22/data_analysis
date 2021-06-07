import argparse
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
                        print(splitLine)
                        line = line[0].split(",")
                        if len(line) > 2:
                            print(line)
                            print(splitLine)
                            if line[2] == splitLine[0]:
                                line[3] = splitLine[1]
                        else:
                            pass
                    else:
                        pass

        with open(result_file, "w") as f:
            for line in text:
                f.write("\t".join(line))
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", help="add the input file", action="store", dest="input_file")
    parser.add_argument("--gene_file", help="add the gene file", action="store", dest="gene_file")
    parser.add_argument("--result_file", help="add the result file", action="store", dest="result_file")
    args = parser.parse_args()
    replaceGenes(args.input_file, args.gene_file, args.result_file)