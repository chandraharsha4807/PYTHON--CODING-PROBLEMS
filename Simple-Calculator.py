n = input()

u = n.split(" ")
operator = u[1]

if operator == "+":
    sum = int(u[0]) + int(u[2])
    print(sum)
elif operator == "-":
    sub = int(u[0]) - int(u[2])
    print(sub)
elif operator == "*":
    multiply = int(u[0]) * int(u[2])
    print(multiply)
elif operator == "/":
    division = int(u[0]) / int(u[2])
    print(int(division))
elif operator == "%":
    module = int(u[0]) % int(u[2])
    print(module)


