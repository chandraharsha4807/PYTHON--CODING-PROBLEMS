def printed_sorted(n):
    print(*sorted(n, key = len))



s = "ABCD ID CR RSTST"
n = sorted(s.split(" "))
printed_sorted(n)



'''
output : CR ID ABCD RSTST

'''