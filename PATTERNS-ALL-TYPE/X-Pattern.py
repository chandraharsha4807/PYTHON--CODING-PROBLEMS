''' X-Pattern '''
def x_pattern(n):
    for i in range(0,n):
        for j in range(0,n):
            if i == j or j == n-i-1:
                print("*", end = "")
            else:
                print(" ", end = "")
        print()

x_pattern(9)