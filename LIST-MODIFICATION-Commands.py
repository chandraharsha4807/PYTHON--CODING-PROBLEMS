if __name__ == '__main__':
    N = int(input())
    
lis=[]
for i in range(N):
    command, *value = input().split()
    #print(command, *value)
    if command == 'print':
        print(lis)
    else:
        getattr(lis,command)(*(map(int, value)))


'''

4 
insert 0 5 
insert 1 10
insert 0 6 
print      
[6, 5, 10]

'''