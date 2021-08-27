sent = input()


sent_list = sent.split(" ")
temp = sent_list

for i in range(len(sent_list)):
    if i%2 == 0 or i == 0:
        temp[i] = (sent_list[i][::-1])

#print(temp)

output = " ".join(map(str, temp)) #list comprehension

print(output)

