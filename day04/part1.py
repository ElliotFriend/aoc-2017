my_input = open('day04\input.txt', 'rt')
any_count = 0
valid_count = 0
for l in my_input:
    any_count += 1
    pass_phrase = l.strip().split(" ")
    if len(pass_phrase) == len(set(pass_phrase)):
        valid_count += 1
print(any_count)
print(valid_count)
