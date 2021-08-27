n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split(" "))))
#print(matrix)
z = []
for i in range(n): 
    if matrix.index(matrix[i]) == i:
        z.append(matrix[i][len(matrix)-i-1])
    
print(z)