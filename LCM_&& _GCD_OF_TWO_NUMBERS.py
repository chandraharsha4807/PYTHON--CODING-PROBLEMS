def gcd(f,s):
    if (s == 0):
        return f
    else:
        return gcd(s, f%s)
def lcm(f,s):
    if (f > s):
        greater = f 
    else:
        greater = s
    while(True):
        if(greater % f == 0 and greater % s == 0):
            output = greater
            break
        greater = greater+1 
    return output

n = list(map(int, input().split()))
f = n[0]
s = n[1]

result = []
result.append(gcd(f,s))
result.append(lcm(f,s))

print(*result) # Gives GCD and LCM as Output

