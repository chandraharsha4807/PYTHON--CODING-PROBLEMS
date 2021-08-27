def overlapping(l,k):
    for char in range(len(str_A)):

 
        if str_B.startswith(str_A[char:]):
            res = str_A[char:]
            #print("\nString A:", str_A)
            #print("String B:", str_B)
            print(str(res))
            break
    else:
        #print("\nString A:", str_A)
        #print("String B:", str_B)
        print ("No overlapping")



str_A = str(input())

str_B = str(input())

overlapping(str_A, str_B)