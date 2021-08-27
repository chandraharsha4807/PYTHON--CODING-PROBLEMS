def divisor(num):

    for i in range(1,num+1):
        if num % i == 0:
        #''' This will give all divisor of give input'''
            print(i)




n = int(input())
r = int(input())
values_of_54 = divisor(n)
values_of_24 = divisor(r)