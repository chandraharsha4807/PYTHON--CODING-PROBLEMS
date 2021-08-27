open_braces = ["[", "{", "("]
close_braces = ["]", "}",")"]

def balanceBrackets(user_string):
    temp = []
    for i in user_string:
        if i in open_braces:
            temp.append(i)
        elif i in close_braces:
            x = close_braces.index(i)
            if (len(temp)> 0) and (open_braces[x] == temp[len(temp)-1]):
                temp.pop()
    if len(temp) == 0:
        print("YES")
    else:
        print("NO")
            
    
user_string = input().split(" ")

for b in range(len(user_string)):
    balanceBrackets(user_string[b])
