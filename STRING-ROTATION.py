n = input()
list1 = list(n.split())
m = list(map(int, input().split()))
L = m[0]
R = m[1]
sente = ""
for words in list1:
    if len(words) > L:
            sente = sente + (words[-(R%(len(words))):] + words[:-(R%(len(words)))]) + " "
    else:
        sente = sente+words+ " "
       
print(sente)