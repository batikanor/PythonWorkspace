import random
import math
# table1 with 100 Buckets

def hash1(key, len):
    return ((3 * key) - 3) % len

def hash2(key, len):
    return ((5 * math.ceil(math.sqrt(key))+ 2)) % len

    

def insert(t1, t2, func1, func2, key, val):
    h = func1(key, len(t1))
    if len(t1[h]) != 0:
        old = t1[h][0]
        t1[h][0] = val
        
        print("--")
        print(t1)
        print(t2)
        print("--")
        insert(t2, t1, func2, func1, old, val)
    else:
        t1[h].append(val)
        print("--")
        print(t1)
        print(t2)
        print("--")
        

def symboltable(tsize, insize):
    table1 = [[] for _ in range(tsize)]
    table2 = [[] for _ in range(tsize)]
    for _ in range(insize):
        i = random.randint(0, insize * 5)
        print("int to add: " + str(i))
        insert(table1, table2, hash1, hash2, i, i)
    print("ENDRESULT!:")
    print(table1)
    print(table2)

# Cuckoo hashing
symboltable(10, 5)


