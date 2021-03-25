import argparse

def find_gene(gene, input_file, output_file):
    gene_list = gene.split(',')
    with open(input_file) as f1:
        with open(output_file, "w") as f2:
            count = 0
            while True:
                if count > 0:
                    line = f1.readline()
                    if not line:
                        break
                    split_line = line.split('\t')
                    genes = split_line[8].split(';')
                    if type(gene_list) == list:
                        for gene in gene_list:
                            try:
                                if gene.strip() == genes[0] or gene.strip == genes[1]:
                                    f2.write(line)
                                    print('ok')
                            except IndexError:
                                if gene.strip() == genes[0]:
                                    f2.write(line)
                                    print('ok')
                            count += 1
                    else:
                        if gene in genes:
                            f2.write(line)
                            print('ok')
                        count += 1
                else:
                    line = f1.readline()
                    f2.write(line)
                    count += 1
    print(count)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--gene_requested", help="add the gene desired", action="store", dest="gene_requested")
    parser.add_argument("--input_file", help="add the file to read", action="store", dest="input_file")
    parser.add_argument("--output_file", help="add the file to write the output in", action="store", dest="output_file")
    args = parser.parse_args()
    find_gene(args.gene_requested, args.input_file, args.output_file)