# There are six sequence types: strings, Unicode strings, lists, tuples, buffers, and xrange objects.

seq = '1234567'
print(seq[::2]) #1357 (start:end:step)

print(seq.find('3')) # 2 (0. index -> 1, 2.index -> 3)

tuple1=("A","B","C")
print(tuple1[-1]) # C

A=((1),[2,3],[4])
print(A[2]) # [4]

B = [1, 2, 3]
B.append(4)
del(B[0])

C = B
C.append(5)
print(B, C) # [2, 3, 4, 5] [2, 3, 4, 5]

D = C[:]
D.append(0)
print(C, D) # [2, 3, 4, 5] [2, 3, 4, 5, 0]


print(len(("disco",10))) # 2 (#items in this tuple)

D.sort()
print(D)