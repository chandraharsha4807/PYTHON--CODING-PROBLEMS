n = int(input())

# input tuples of Pi and Ci
PiCi = []
for i in range(n):
    l = input().split()
    Pi = int(l[0])
    Ci = int(l[1])
    PiCi.append((Pi, Ci))

PiCi.sort(reverse=True)
first = True
for Pi, Ci in PiCi:
    
    # print Coefficent
    if Ci == 0:
        continue
    elif Ci == 1:
         print(" + ",end = '')
    elif Ci < 0.0:
        if first:
            print(Ci, end='')
        elif Ci == -1:
            print(' - ', end = '')
        else:
            print(' -', abs(Ci), end='')
    else:            
        if first:
            print(Ci, end='')
        else:
            print(' +', abs(Ci), end='')
    first = False
    
    # print x^Pi
    if Pi == 0:
        continue
    elif Pi == 1:
        print("x", end = '' )
    elif Pi < 0:
        print(f'x^{Pi}', end='')
    else:
        print(f'x^{Pi}', end='')        
        
print()