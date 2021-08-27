def factorial(n):    
    if n == 1 or n == 0:
        #print(n)
        return 1    
    else:
        #print (n,'*', end=' ')
        return n * factorial(n-1)

n = int(input())
print(factorial(n))

'''


num = int(input())


factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i

print(factorial)


'''