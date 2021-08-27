n = int(input())
m = int(input())
list1 = []
for i in range(n, m+1):
     for j in range (2, m):
         if i/j == j: # gives perfect square number
             #print(i,j)
             list1.append(i)
        
#print(list1)

if len(list1) != 0:
    list1.sort()
    print(list1[0])
else:
    print("No Perfect Square")
