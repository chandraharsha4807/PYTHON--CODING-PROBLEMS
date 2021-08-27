'''Finding the difference between the sum of odd and even numbers fom a list of 5'''
'''
   INPUT
   input1 5
   input2 10 11 7 12 14
   Output
   -18
'''

n = int(input())
list = []
for i in range (n):
    m = int(input())
    list.append(m)

#print(list)

even_list = []
odd_list =[]
for num in list:
    if num%2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

#print(even_list)
#print(odd_list)
sum_even =0
sum_odd =0 
for elem in range(0,len(even_list)):
    sum_even = sum_even + even_list[elem]

for elem in range(0, len(odd_list)):
    sum_odd = sum_odd + odd_list[elem]

print(sum_odd - sum_even)