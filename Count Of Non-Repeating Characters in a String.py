
str=input("Enter Your String:").lower()
arr=[0]*256
for i in range(len(str)):
    if str[i]!=' ':
        num=ord(str[i])
        arr[num]+=1
l = []
print("All Non-repeating character in a given string is: ",end="")
for i in range(len(str)):
        if arr[ord(str[i])] ==1:
            l.append(str[i])

print(len(l))


'''

Input - Enter Your String:Alphaadida
Output - All Non-repeating character in a given string is: 4


'''