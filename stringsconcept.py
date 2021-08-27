# input string "Hello World"
string = 'This is my first HelloWorld Program and existed to code it'
# to get first character of string at the end
new_string = string[1:] + string[0]
# output string "ello worldH"
print(new_string)


## string partition is used grab values at specified index
res = string.partition('HelloWorld')
# (or) res = string.partition('HelloWorld)[2]

# output = remaining words from the "HelloWorld" 
# output = Program and existed to code it
print(res[2])

