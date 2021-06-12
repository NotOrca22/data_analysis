import bs4 as BeautifulSoup
import mechanize

import requests
import argparse
genes= {}
def removeDuplicates(input_file, gene_file, result_file):
    with open(input_file) as f:
        line = f.readline()
        # print(line)
        namesFound = set()

        while line:
            line = f.readline()
            arr = line.split(",")
            # print(arr)
            if len(arr) > 1:
                namesFound.add(arr[2].strip('"'))

        # print(indexes)
        br = mechanize.Browser()
        br.open("https://www.biotools.fr/human/refseq_symbol_converter")
        br.select_form(nr=0)
        print(br.form)
        br.form['input_data'] = "\n".join(namesFound)
        print(br.form)
        req = br.submit()
        res = str(req.read())
        # res = res.decode()
        res = res.split("\\n")
        print(res)
        with open("genes.txt", "w") as f:
            for x in res[:len(namesFound)]:
                x = x.split("\t")
                genes[x[0]] = x[1]
def replaceGenes(input_file, genes, result_file):
    text = []
    with open(input_file) as file:
        line = "orca"
        while line:
            line = file.readline()
            if line:
                text.append(line.split(" "))
        splitLine = line.split("\t")
        for line in text:
            if len(splitLine) > 1:
                line = line[0].split(",")
                if len(line) > 2:
                    if line[2] == splitLine[0]:
                        line[3] = splitLine[1]
                    else:
                        pass
                else:
                    pass

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
    removeDuplicates(args.input_file, "genes.txt", args.result_file)
    replaceGenes(args.input_file, genes, args.result_file)
