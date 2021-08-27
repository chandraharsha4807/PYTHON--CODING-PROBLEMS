''' Word Count-2 '''
n = input()

word_n = n.split()
print(word_n)
word_n.sort()

temp_str = []
for i in word_n:
    if i not in temp_str:
        temp_str.append(i)
        #print(temp_str)
temp_str.sort()
for i in range(len(temp_str)):
    print(temp_str[i] + ": " + str(word_n.count(temp_str[i]))) 
    #print (words_n.count(temp_str[i]))
