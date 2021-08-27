def CountCurrency(N):
    notes = [1000, 500, 100, 50, 20, 10, 1]
    while N>0:
        
        for i in range(0, len(notes)):
            j = 0
            if N >= notes[i]:
                j = int(N/notes[i])
                
            print("{}".format(notes[i])+":{}".format(j))
            N = N % notes[i]
    
    
N = int(input())

CountCurrency(N) 
