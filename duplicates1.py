import argparse
def removeDuplicates(input_file, result_file):
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
        with open(result_file, "w") as f:
            f.write("\n".join(namesFound))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", help="add the input file", action="store", dest="input_file")
    # parser.add_argument("--output_file", help="add the output file", action="store", dest="output_file")
    # parser.add_argument("--gene_file", help="add the gene file", action="store", dest="gene_file")
    parser.add_argument("--result_file", help="add the result file", action="store", dest="result_file")
    args = parser.parse_args()
    removeDuplicates(args.input_file, args.result_file)
