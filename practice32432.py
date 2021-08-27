def is_square(matrix, lt_i, lt_j, side_length):
    for i in range(lt_i, lt_i+side_length):
        for j in range(lt_j, lt_j+side_length):
            if matrix[i][j] != "X":
                return False
    return True


n = list(map(int,input().split(" ")))
#print(n)
matrix = []
for i in range(n[0]):
    matrix.append(input().split(" "))

#print(is_square(matrix, 1, 2, 3))

areas = [0]

for i in range(n[0]):
    for j in range(n[1]):
        right_end = n[1] - j 
        bottom_end = n[0] - i 
        max_side_length = min(right_end, bottom_end)
        for side_length in range(1, max_side_length+1):
            if is_square(matrix, i, j, side_length):
                area = side_length * side_length
                areas.append(area)
#print(areas)
print(max(areas))