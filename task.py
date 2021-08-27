def query_game(N, A, Q, P):
    # print(N)
    # print(A)
    # print(Q)
    # print(P)
    r = []
    for l in P:
        if l[0] == 1:
            #print("type 1")
            r = A[::-1]
            print(r)
            
            
        if l[0] == 2:
            #print("type 2")
            A[l[1]-1], A[l[2]-1] = A[l[2]-1], A[l[1]-1]
            r = A
            #print(r)
            

        if l[0] == 3:
            #print("type 3")
            print(A)
            r = A[l[1]]
            #print(r)

    print(r)
    

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    P = [list(map(int, input().split())) for i in range(Q)]

    out = query_game(N, A, Q, P)
