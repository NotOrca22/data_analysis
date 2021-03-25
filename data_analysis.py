import argparse
def extract_columns(input_filename_1, input_filename_2, output_filename):
    splitlines2 = []
    counter = 0

    with open(input_filename_1) as f1:
        with open(input_filename_2) as f2:
            with open(output_filename, "w") as output_file:
                while True:
                    line = f1.readline()
                    if not line:
                        break
                    columns = line.split('\t')[17:]
                    print(columns)
                    line2 = f2.readline()
                    entry = columns[0].split(':')
                    print(entry[1])
                    fields = entry[1].split(',')
                    if len(fields) == 2:
                        AD = fields[1]
                        RD = fields[0]
                    else:
                        continue
                    DP = int(entry[2])
                    if DP == 0:
                        continue
                    FREQ = "{:.2f}".format(int(AD)/int(DP))
                    line2 = line2.replace('\n', '')
                    if counter > 0:
                        output_file.write(line2 + '\t' + str(RD) + '\t' + str(AD) + '\t' + str(DP) + '\t' + str(FREQ) + '\n')
                    else:
                        output_file.write(
                            line2 + '\t' + 'RD' + '\t' + 'AD' + '\t' + 'DP' + '\t' + 'FREQ' + '\n')
                    counter += 1
                print(counter)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", help="add the input file", action="store", dest="input_file")
    parser.add_argument("--output_file", help="add the output file", action="store", dest="output_file")
    parser.add_argument("--read_file", help="add the read file", action="store", dest="read_file")
    args = parser.parse_args()
    extract_columns(args.input_file, args.read_file, args.output_file)