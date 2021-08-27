'''
n = int(input())
m = int(input())

for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1 or j == 0 or j == m-1:
             print("* ",end = "")
        else:
              print(" ", end=" ")

    print()

'''

rows = int(input())
columns = int(input())

for i in range(rows):
    if (i == 0) or (i == (rows - 1)):
        print("* " * columns)
    else:
        number_of_spaces = ("  " * (columns - 2))
        print("* " + number_of_spaces + "*")