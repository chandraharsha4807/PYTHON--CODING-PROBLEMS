''' Finding the total distance between adjacent items of a list'''


n = int(input())
list = list(map(int,input().split()))

sum = 0
for i in range(n-1):
    sum += abs(list[i]- list[i+1])
print(sum)

'''
input1 5
input2 10 11 7 12 14

output
12

'''