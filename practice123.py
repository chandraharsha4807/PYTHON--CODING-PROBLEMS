def combinations(a, r):
    list1 = []
    a.sort()
    if r == 0:
        return [[]]
    for i in range (len(a)):
        m = a[i]
        remlst = a[i+1:]
        comblist = combinations(remlst, r-1)
        #print(comblist)
        for j in comblist:
            list1.append(([m]+j))   
    return list1
                

                 


a = list(map(int, input().split()))
new_list = []
for i in range(1,len(a)+1):
    new_list.append(tuple(combinations(a,i)))

print(new_list)

