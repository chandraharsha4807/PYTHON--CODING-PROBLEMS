def gcd (a,b):

    if(b==0):

        return a

    else:

        return gcd(b,a % b)
        # "( a % b )" will gives the remainder which is greatest common divisor

a=int(input("Enter first number:"))

b=int(input("Enter second number:"))

GCD=gcd(a,b)

print("GCD of ",a," and ",b,"is:",GCD)