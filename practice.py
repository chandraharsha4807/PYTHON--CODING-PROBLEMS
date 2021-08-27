
sent = input()
#print(len(sent))
z = []
for x in range(len(sent)):
    if sent[x].isdigit() == True:
        if x == 0:
            z.append(sent[x])
            
        elif sent[x - 1].isdigit() == True:
            z[-1] += sent[x]
        else:
            z.append(sent[x])
            #print(z)

#print(z)


k = 0
for n in z:
    k += int(n)
print(k)

print(round(k / len(z),2))