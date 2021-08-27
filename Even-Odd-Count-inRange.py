def odd_numbers_count(M, N):
    count = 0
    for num in range(M, N+1):
        if num % 2 != 0:
            count += 1
    print(count)
    
    
def even_numbers_count(M, N):
    count = 0
    for num in range(M, N+1):
        if num % 2 == 0:
            count += 1
    print(count)


M = int(input())
N = int(input())
odd_numbers_count(M, N)
even_numbers_count(M, N)