word=input().split()
n=int(input())
a=""
for i in word:
    a=a+i
b=a[-n:]+a[:-n]


k=0
l=0
result=[]
for i in word:
    l=l+len(i)
    result.append(b[k:l])
    k=k+len(i)
    
print(" ".join(result))