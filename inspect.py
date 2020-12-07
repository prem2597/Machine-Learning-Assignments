import math
import sys
import csv

label1 = 0
label2 = 0

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    x = ''
    for row in csv_reader:
        if line_count != 0:
            if label1 == 0 and label2 == 0:
                x = row[-1]
            if row[-1] == x:
                label1 += 1
            else:
                label2 += 1
        line_count += 1

# print(line_count)
# print(label1)
# print(label2)

total = label1 + label2

probability1 = label1 / total
probability2 = label2 / total

entropy = - probability1 * math.log2(probability1) - probability2 * math.log2(probability2)

if label1 >= label2 :
    error_rate = probability2
else :
    error_rate = probability1

# print(entropy)
# print(error_rate)

with open(sys.argv[2], 'w') as output_file:
    output_file.write(f'entropy: {entropy}\nerror: {error_rate}')


