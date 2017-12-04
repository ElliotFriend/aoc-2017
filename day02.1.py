import csv

my_input = list(csv.reader(open('day02.input.txt', 'rt'), delimiter='\t'))
my_checksum_list = []
#print(my_input)

for i in range(0, len(my_input)):
    my_input_line = sorted([int(x) for x in my_input[i]])
    print(sorted(my_input_line))
    my_checksum_list.append(int(my_input_line[-1]) - int(my_input_line[0]))

print(sum(my_checksum_list))
