num_list = list(map(int, input().split(" ")))

negative_list = []
for num in num_list:
    if num < 0:
       negative_list.append(num)

negative_list.sort(reverse=True)
print(negative_list)
temp = -1
for i in range(len(negative_list)):
       if temp > negative_list[i]:
           break
       temp = negative_list[i] -1

print(temp)
    
