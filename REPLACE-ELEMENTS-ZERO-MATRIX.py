
n = input().split(" ")

rows = int(n[0])
col = int(n[1])
matrix = []
for i in range(0, rows):
    matrix.append([int(col) for col in input().split()])

#print(matrix)

for i in range(len(matrix)):
    for j in range(col):
        if i != j and i+j != col-1:
            matrix[i][j]=0
#print(matrix)


for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end = " ")
    print( )


'''

10 10
73 18 100 29 91 98 5 45 16 18
73 18 100 29 91 98 5 45 16 18
73 18 100 29 91 98 5 45 16 18
73 18 100 29 91 98 5 45 16 18
73 18 100 29 91 98 5 45 16 18
73 18 100 29 91 98 5 45 16 18
73 18 100 29 91 98 5 45 16 18
73 18 100 29 91 98 5 45 16 18
73 18 100 29 91 98 5 45 16 18
73 18 100 29 91 98 5 45 16 18

OUTPUT

73 0 0 0 0 0 0 0 0 18 
0 18 0 0 0 0 0 0 16 0
0 0 100 0 0 0 0 45 0 0
0 0 0 29 0 0 5 0 0 0
0 0 0 0 91 98 0 0 0 0
0 0 0 0 91 98 0 0 0 0
0 0 0 29 0 0 5 0 0 0
0 0 100 0 0 0 0 45 0 0
0 18 0 0 0 0 0 0 16 0
73 0 0 0 0 0 0 0 0 18

'''
