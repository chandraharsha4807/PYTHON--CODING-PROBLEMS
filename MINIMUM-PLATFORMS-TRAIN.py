'''
0900 0940 0950 1100 1500 1800
0910 1200 1120 1130 1900 2000

[900, 910, 940, 950, 1100, 1120, 1130, 1200, 1500, 1800, 1900, 2000]

[1, 0, 1, 2, 3, 2, 1, 0, 1, 2, 1, 0] 
maximum of list will give minimum number of platforms output = 3

0900 1100 1235
1000 1200 1240

[900, 1000, 1100, 1200, 1235, 1240] 

[1, 0, 1, 0, 1, 0]
maximum of list will give minimum number of platforms output = 1
'''
def minimum_platform(comb, d_time):
    count = 0
    count_list = []

    for i in comb:
        if i not in d_time:
            count+= 1
            count_list.append(count)
        else:
            count-=1
            count_list.append(count)
    print(max(count_list))

a_time = list(map(int, input().split()))
d_time = list(map(int, input().split()))

#print(a_time)
#print(d_time)
comb = a_time+d_time
comb.sort()
#print(comb)

minimum_platform(comb, d_time)
