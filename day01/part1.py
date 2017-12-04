my_input = 1122
my_input_list = [int(d) for d in str(my_input)]
my_adding_list = []

for x in range(-1, len(my_input_list) - 1):
    if my_input_list[x] == my_input_list[x + 1]:
        my_adding_list.append(my_input_list[x])

print(sum(my_adding_list))
