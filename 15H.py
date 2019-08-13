ax=int(input())
s=list(map(int,input().split()))
v=0
n=[]
f=[]
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        if A[i]<A[j]:
            v=v+1
            break
    else:
        n.append(s[i])        
print(*n)
print(max(s))
