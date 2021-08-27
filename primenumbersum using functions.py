def prime(n): 
	''' This function takes a number and return a string whether or not it is a prime or not''' 
	if n <= 0: 
		return "Not defined" 
	elif n == 1:
		return "not prime"
	for i in range(2,n):
		if n%i == 0:
			return "not prime"
	return "prime"

 
 
def add_prime(num):
	''' This function is for summing up the prime numbers'''
	total = 0
	for i in range(2, num+1):
		x = prime(i)
		if x == "prime":
			''' Here "i" will print prime number '''
			#print(i)
			total += i
			#print(total)
	return total

num = int(input())

print(add_prime(num))
#print(prime(num))