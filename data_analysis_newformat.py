import argparse
from datetime import datetime
def get_data(input_filename, read_filename, output_filename):
    counter = 0
    current_time = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
    with open(input_filename) as f1:
        with open(read_filename) as f2:
            with open(output_filename + '_' + current_time + '.txt', "w") as output_file:
                while True:
                    line = f1.readline()
                    if not line:
                        break
                    line = line.split('\t')
                    RD, AD = line[-1].split(':')[1].split(',')
                    DP = int(RD) + int(AD)
                    FREQ = "{:.2f}".format(int(AD) / int(DP))
                    line2 = f2.readline()
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
    get_data(args.input_file, args.read_file, args.output_file)