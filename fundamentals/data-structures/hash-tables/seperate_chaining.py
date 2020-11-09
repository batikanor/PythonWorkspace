__author__ = "BATIKAN BORA ORMANCI"

import random


def hashfunc(num, buckets):
    return num % buckets
def insert(table, key, val):
    insertkey = hashfunc(key, len(table))
    table[insertkey].append(val)
            
def sepchaining(ints_count):
    print(f"FOR {ints_count} RANDOM INTEGERS")
    buckets_count = int(ints_count / 100)
    hash_table = [[] for _ in range(buckets_count)]
    for _ in range(ints_count):
        # Python 3's int doesn't have a max size, so I'll use the range for ints in c 
        newrand = random.randint(-2147483648, 2147483647)
        # newrand = random.randint(0, 3)
        insert(hash_table, newrand, newrand)
    # print(hash_table)
    # find Length of the longest and shortest lists
    shortest = 2147483647
    longest = -1
    for row in hash_table:
        if len(row) > longest:
            longest = len(row)
        elif len(row) < shortest:
            shortest = len(row)
    print(f"Shortest = {shortest} and Longest = {longest}")


# N = 10^3
sepchaining(1000)

# N = 10^4
sepchaining(10000)

# N = 10^5
sepchaining(100000)

# N = 10^6
sepchaining(1000000)


