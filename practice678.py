# Python3 program to find the minimum
def getMinJumps(s):
	# Store all indices
	ones = []
	jumps, median, ind = 0, 0, 0
	# Populating one's indices
	for i in range(len(s)):
		if(s[i] == '1'):
			ones.append(i)

	if(len(ones) == 0):
		return jumps
	# Calculate median
	median = ones[len(ones) // 2]
	ind = median
	# Jumps required for 1's
	# to the left of median
	for i in range(ind, -1, -1):
		if(s[i] == '1'):
			jumps += ind - i
			ind -= 1

	ind = median
	# Jumps required for 1's
	# to the right of median
	for i in range(ind, len(s)):
		if(s[i] == '1'):
			jumps += i - ind
			ind += 1
	# Return the final answer
	return jumps
# Driver Cod
s = input()
	
print(getMinJumps(s))

# This code is contributed by Shivam Singh
