import csv

my_input = list(csv.reader(open('day02\input.txt', 'rt'), delimiter='\t'))
my_checksum_list = []

for i in range(0, len(my_input)):
    my_input_line = sorted([int(x) for x in my_input[i]])
    for x in my_input_line:
        for n in my_input_line:
            if x != n:
                if x % n == 0:
                    # boy did this get nested and ugly :-\
                    my_checksum_list.append(x / n)

print(sum(my_checksum_list))
