n = int(input())

for i in range(n):
    num = i+1
    dec = n-1
    for j in range(i + 1):
        print(num, end = " ")
        num = num + dec
        dec = dec-1
    print()
  
'''

Input : 5

1         
2 6       
3 7 10    
4 8 11 13 
5 9 12 14 15

'''