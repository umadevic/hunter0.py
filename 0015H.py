ax=int(input())
A=list(map(int,input().split()))
h=0
p=[]
d=[]
for i in range(0,len(A)):
    for j in range(i+1,len(A)):
        if A[i]<A[j]:
            h=h+1
            break
    else:
        p.append(A[i])        
print(*p)
print(max(A))

