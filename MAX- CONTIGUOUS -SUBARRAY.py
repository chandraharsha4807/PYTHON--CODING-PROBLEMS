a = list(map(int, input().split()))

if not a:
    print(0)
else:
    sum_dict = {}
    for i in range (len(a)):
        for j in range(i+1, len(a)+1):
            sum_dict[tuple(a[i:j])] = sum(a[i:j])
            #print(tuple(a[i:j]))
            #print(sum_dict[tuple(a[i:j])])
            #print(a[i:j])
            #print(tuple(a[i:j]),sum(a[i:j]))
    
    #print(sum_dict.keys())
    #print(sum_dict.values())
    keys = list(sum_dict.keys())
    print(keys)
    values = list(sum_dict.values())
    #print(values)
    
    max_sum_index = values.index(max(values))
    #print(max_sum_index)
    print(*keys[max_sum_index])


'''
Given a list of integers, 
write a program to identify contiguous sub-list that has the largest sum and print the sub-list. 
Any non-empty slice of the list with step size 1 can be considered as contiguous sub-list.

For example, if the given list is [2, -4, 5, -1, 2, -3], then all the possible contiguous sub-lists will be,
[2]
[2, -4]
[2, -4, 5]
[2, -4, 5, -1]
[2, -4, 5, -1, 2]
[2, -4, 5, -1, 2, -3]
[-4]
[-4, 5]
[-4, 5, -1]
[-4, 5, -1, 2]
[-4, 5, -1, 2, -3]
[5]
[5, -1]
[5, -1, 2]
[5, -1, 2, -3]
[-1]
[-1, 2]
[-1, 2, -3]
[2]
[2, -3]
[-3]

INPUT
2 -4 5 -1 2 -3

OUTPUT
5 -1 2

'''