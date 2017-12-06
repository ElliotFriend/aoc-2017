import zlib
import binascii
import operator

def MemoryBankHash(memory_bank):
    return zlib.crc32(binascii.a2b_qp("".join(str(i) for i in memory_bank)))

with open('day06/input.txt', 'rt') as file:
    for line in file:
        my_memory_bank = list(map(int, line.strip().split("\t")))
file.close()

my_memory_bank_hash = MemoryBankHash(my_memory_bank)
my_crc_hashes = []

while my_memory_bank_hash not in my_crc_hashes:
    bank_location, block_amount = max(enumerate(my_memory_bank), key=operator.itemgetter(1))
    my_new_bank = my_memory_bank
    my_new_bank[bank_location] = 0

    while block_amount > 0:
        if len(my_new_bank) - 1 > bank_location:
            bank_location += 1
        else:
            bank_location = 0
        my_new_bank[bank_location] += 1
        block_amount -= 1

    my_crc_hashes.append(my_memory_bank_hash)
    my_memory_bank_hash = MemoryBankHash(my_new_bank)
    my_memory_bank = my_new_bank

print("Redistribution Count: ", len(my_crc_hashes))
