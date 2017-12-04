my_input = open('day04.input.txt', 'rt')
any_count = 0
valid_count = 0
for l in my_input:
    any_count += 1
    pass_phrase = l.strip().split(" ")
    if len(pass_phrase) == len(set(pass_phrase)):
        phrase_words = []
        for w in pass_phrase:
            w = sorted(w)
            phrase_words.append("".join(w))
        if len(phrase_words) == len(set(phrase_words)):
            valid_count += 1
print("all: ",any_count)
print("valid: ",valid_count)
