n = list(map(int, input().split(" ")))
f = int(n[0])
s = int(n[1])

for i in range(1, f+1):
    lf = " "*s*(f-i)
    print(lf + "*"*f)


'''
Parallelogram
Write a program to print a parallelogram pattern with * characters. The size N  represents the length (the number of * characters in each line) & breadth (the number of lines) of the parallelogram.

The slope of the parallelogram T represents the number of
extra spaces a line should have in the beginning compared to its next line.
The last line of the pattern does not have any spaces in the beginning.

Input

The input contains an integer N.

Output

The output should have N lines. Each line should have spaces followed by N number of * characters as mentioned above.

Explanation
Given N = 3 and T = 2.

Each line should have 3 star(*) characters.
The last line should have 0 spaces at the beginning.
Each line has 2 extra space characters when compared to its next line.


4 3
         ****
      ****
   ****
****

3 2
    ***
  ***
***

'''