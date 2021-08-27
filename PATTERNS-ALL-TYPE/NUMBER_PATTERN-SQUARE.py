# METHOD -1
n = int(input())

for i in range(n):
    for j in range(n):
        print((str(j+1)+" "), end = "")
    print()
    
'''
# METHOD-2
n = int(input())

pattern = ""

for i in range(n):
    pattern = pattern + (str(i+1) + " ")

for i in range(n):
    print(pattern)

'''

'''

5
1 2 3 4 5 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

'''