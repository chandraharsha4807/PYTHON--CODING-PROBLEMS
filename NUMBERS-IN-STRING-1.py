sentence = input()
#print(sentence)
num_list = []
for char in sentence:
    if char.isdigit() == True:
        num_list.append(int(char))
#print(num_list)

print(sum(num_list))
avg = sum(num_list)/len(num_list)
print(round(avg, 2))