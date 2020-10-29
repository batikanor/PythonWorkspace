A=['1','2','3']

for a in A:
  print(2*a)


myList = ['A','B','C']

for i,x in enumerate(myList):
    print(i,2*x)

print(myList)
print(enumerate(myList)) # The enumerate object yields pairs containing a count (from start, which
#> defaults to zero) and a value yielded by the iterable argument.
#> enumerate is useful for obtaining an indexed list:
#> (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

for i in range(1,5):
    if (i==2):
        print(i)


squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares) # Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':
