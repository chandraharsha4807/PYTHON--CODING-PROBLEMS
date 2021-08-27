def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
     
    else:
        return False
        
n = int(input())
nums = []
for x in range(n):
    nums.append(int(input())) # append is used to add single item to existing list


sum = 0
for num in nums:
    if(not isPrime(num)):
        sum = sum + num
print(sum)


'''for num in nums:
    if (num == nums[n-1]):
        if( not isPrime(num)):
            print(num, " = ", sum,end="")
    else:
        if(not isPrime(num)):
            print(num, " + ", end="")'''