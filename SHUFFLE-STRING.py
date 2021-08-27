word = input()
length = len(word)
new_word = ""
for i in range (length):
    n = int(input())
    new_word = new_word + word[n]
    
print(new_word)

'''

For example, if the given string is "goindc", 
then read the inputs in the next six lines (length of the string is six). 
If the given input integers in the next six lines are 5, 1, 4, 2, 3, and 0. 
By shuffling the word as per the given order

5 - c

1 - o

4 - d

2 - i

3 - n

o - g

the output should be "coding".

'''