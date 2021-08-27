n = int(input())
for i in range(n-1):  # i = 0,1,2 for n = 3
     print("  "*(n-i-1) +chr(65+i)+ " ", end = "")
     if i >= 1:
          print("  "*((2*i)-1) + chr(65+i), end = "")
     print()

for j in range(n):
     print("  "*j + chr(65+n-j-1) +" ", end = "")
     if j!= n-1:
          print("  "*(((2*n) - (2*j) -3))+ chr(65+n-j-1) + " ", end= "")
     print()

     
     

