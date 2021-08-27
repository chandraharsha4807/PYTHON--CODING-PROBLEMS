''' Anti -Diagonal Elements of Matrix '''
def diagonal(A) :
 
    n = len(A)
    #print(n)
    N = 2 * n - 1
 
    result = []
     
    for i in range(N+1) :
        result.append([])
        #print(result)
     
    # Push each element in the result vector
    for i in range(n) :
        for j in range(len(A[0])) :
            result[i + j].append(A[i][j])
            #print(result)
 
    # Print the diagonals
    for i in range(len(result)) :
     
        for j in range(len(result[i])) :
            print(result[i][j] , end = " ")
             
        print()


n = input()
RC = n.split()
rows = int(RC[0])
columns = int(RC[1])

matrix = []

for i in range(0, rows):
    matrix.append([int(j) for j in input().split()])
#print(matrix)



diagonal(matrix)