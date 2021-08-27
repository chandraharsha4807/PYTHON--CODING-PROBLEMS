n = list(map(int, input().split()))
f = n[0]
s = n[1]

matrix = []
for i in range(f):
    matrix.append(list(map(int,input().split(" "))))
#print(matrix)

for i in range(len(matrix)):
    if (i%2 != 0):
        matrix[i] == matrix[i].reverse()
    else:
        matrix[i] = matrix[i]
        
#print(matrix)

out = []
for i in matrix:
    for j in range(len(i)):
        out.append(i[j])
print(*out)


'''

First Line Input : 4 4

Next 4 Lines of Input
1 2 3 4
5 6 7 8   
9 10 11 12
13 14 15  

Output:
1 2 3 4 8 7 6 5 9 10 11 12 15 14 13

'''