num = int(input())

if num >1:
    for i in range(2, num): ## SQUARE ROOT int(num**0.5))
        if(num%i == 0):
            print("Not a Prime Number")
            #print(i,"times",num//i,"is",num)
            break
    else:
            print("Prime Number")
else:
    print("Not a Prime Number")


'''
4
Not a Prime Number

'''