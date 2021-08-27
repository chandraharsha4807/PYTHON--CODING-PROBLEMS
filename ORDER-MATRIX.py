

n = input().split(" ")

rows = int(n[0])
col = int(n[1])
matrix = []
for i in range(0, rows):
    matrix.append(sorted([int(col) for col in input().split()]))

#print((matrix))

# Create an empty list to store matrix values
temp = []
for i in range (rows):
    for j in range(col):
        temp.append(matrix[i][j])

#print(sorted(temp))
temp.sort()

# coping elements in temp to matrix[i][j]
k = 0
for i in range(rows):
    for j in range(col):
        matrix[i][j] = temp[k]
        k += 1
#print(matrix)

for i in range(rows):
    for j in range(col):
        print(matrix[i][j], end = " ")
    print(" ")



'''

3 3
1 20 3 
30 10 2
5 11 15
1 2 3     
5 10 11   
15 20 30 

'''