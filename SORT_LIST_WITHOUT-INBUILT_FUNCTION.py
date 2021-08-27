List1 = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34, 1]
#List2 = ['e', 'd', 'c', 'b', 'a']

for i in range(len(List1)):
    for j in range(i + 1, len(List1)):
        if List1[i] > List1[j]:
           List1[i], List1[j] = List1[j], List1[i]

print (List1)