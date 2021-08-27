n = int(input())
list1 =[]
for i in range(1,n+1):
   list1.append(i)
#print(list1)

for i in range(len(list1)):
   for j in range(i+1, len(list1)):
      if j < len(list1):
         list1.pop(j)
         print(list1)
#print(list1)

if n in list1:
   print("Yes")

else:
   print("No")