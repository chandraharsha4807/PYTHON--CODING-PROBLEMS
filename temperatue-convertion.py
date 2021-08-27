''' Temperature Covertion'''
def temperature_convertion(temp):
    units = temp[-1]
    value = (temp[:-1])
    #value = int(value)
    if units == "C":
        value = float(value)
        F = ((9*value)/5 + 32)
        K = value + 273
        print("{}C".format(value))
        print("{}F".format(round(F)))
        print("{}K".format(round(K,2)))
    elif units == "F":
        value = float(value)
        C = (((value - 32)*5)/9)
        K = C + 273
        print("{}C".format(round(C,2)))
        print("{}F".format((value)))
        print("{}K".format(round(K,2)))
    elif units == "K":
        value = float(value)
        C = (value - 273)
        F = ((9*C)/5 + 32)
        print("{}C".format(round(C,2)))
        print("{}F".format(round(F,2)))
        print("{}K".format((value)))
        
        
temp = input()
temperature_convertion(temp)