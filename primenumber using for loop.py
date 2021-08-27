# Take input from user
n = int(input())

sum = 0

for num in range(2,n+1):
    #print(num)
    i = 0
    for i in range(2, num):
        if (int(num % i) == 0):
            i = num
            #print(i)
            break;

    #If the number is prime then add it.
    if i is not num:
        #print(num)
        sum += num
        #print(sum)

    print("\nSum of all prime numbers upto", i, ":", sum)
            