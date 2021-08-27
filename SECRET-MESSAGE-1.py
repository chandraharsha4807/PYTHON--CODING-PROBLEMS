s = input()
n = s.lower()
list1 = list(map(chr, range(97,123)))
list2 = list(map(int, range(1,27)))
list3 = chr(32)

#print(list1)
#print(new_list2)
string = ""
for char  in n:
    if char in list1:
        index1 = list1.index(char)
        string = string + list2[index1]
    elif char in list2:
        index2 = list2.index(char)
        string = string + list1[index2]
    elif char == list3:
        string = string + " "
print(string)

'''
INPUT : python list
OUTPUT : kbgslm orhg

 '''