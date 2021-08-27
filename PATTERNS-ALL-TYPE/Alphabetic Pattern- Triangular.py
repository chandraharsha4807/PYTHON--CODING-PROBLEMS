n = int(input())

for i in range (1,n+1):
    for j in range(65, 65+i):
        print(chr(j), end = " ")# by changing i in place of "j" we get another pattern
    print()# this print is used for next line printing until "n+1"


'''                  
A
A B
A B C
A B C D          

'''
'''
A
B B
C C C
D D D D

'''