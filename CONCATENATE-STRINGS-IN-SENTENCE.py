sent = input()

n = int(input())

sent_list = sent.split(" ")
list_1 = []

for i in range(len(sent_list)):
    for j in range(len(sent_list)):
        if i == j or sent_list[i] == sent_list[j]:
            pass 
        else:
            s = sent_list[i] + sent_list[j]
            list_1.append(s)

d = list(set(list_1))

sorted_list = sorted(d)
#print(sorted_list)
for words in sorted_list:
    if len(words) == n:
        print(words)