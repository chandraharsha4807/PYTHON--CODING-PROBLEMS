''' word count '''

n = input()

words_n = n.split()
temp_str = []

for i in words_n:
    if i not in temp_str:
        temp_str.append(i)
        #print(type(temp_str))
        #print(temp_str)

for i in range(len(temp_str)):
    print(temp_str[i] + ": " + str(words_n.count(temp_str[i]))) 
    #print (words_n.count(temp_str[i]))
