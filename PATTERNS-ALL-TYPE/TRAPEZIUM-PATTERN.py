num = int(input())

left_value = 1
right_value = num*num+1
for i in range(num, -1, -1):
    for sp in range(num, i, -1):
        print(" ", end = " ")
    for j in range(1, i+1):
        print(left_value, end = " ")
        left_value += 1 
    for j in range(1, i+1):
        print(right_value, end = " ")
        right_value += 1 
        
    right_value = right_value - (i-1) * 2 -1 
    print()

'''
Input : 5

1 2 3 4 5 26 27 28 29 30 
  6 7 8 9 22 23 24 25    
    10 11 12 19 20 21    
      13 14 17 18        
        15 16

'''
