n = list(map(int, input().split()))
n.sort()
result_list = []
for i in range(len(n)):
        #print(i+1, n[i])
        if i+1 != n[i]:
            result_list.append(i+1)

print(result_list[0])