s = input()
n = s.lower()
#print(n)
list1 = list(map(chr, range(97,123)))
list2 = list(map(int, range(1,27)))
list3 = chr(32)

#print(list1)
#print(list2)

l  = []
for char  in n:
    s = ((n.index(char))+1)
    if char in list1:
            index1 = list1.index(char)
            l.append(str(list2[index1]))
            
    elif char == list3:
         l.append(" ")


print(l)
print("-".join(l))
        




