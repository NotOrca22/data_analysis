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
                        AD = fields[0]
                        RD = fields[1]
                    else:
                        continue
                    DP = int(entry[2])
                    if DP == 0:
                        continue
                    FREQ = "{:.2f}".format(int(AD)/int(DP))
                    line2 = line2.replace('\n', '')
                    if counter > 0:
                        output_file.write(line2 + '\t' + str(AD) + '\t' + str(RD) + '\t' + str(DP) + '\t' + str(FREQ) + '\n')
                    else:
                        output_file.write(
                            line2 + '\t' + 'AD' + '\t' + 'RD' + '\t' + 'DP' + '\t' + 'FREQ' + '\n')
                    counter += 1
                print(counter)


if __name__ == '__main__':
    columns = extract_columns("/Users/hailongwang/git/chris/data_analysis/WiHe_germline_exome.strictFilter_PASS.avinput", "/Users/hailongwang/git/chris/data_analysis/WiHe_germline_exome.strictFilter.snp.hg19_multianno.txt", "/Users/hailongwang/git/chris/data_analysis/chris_result.txt")
    print('done1')