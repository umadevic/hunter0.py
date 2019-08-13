b,K=map(int,input().split())
u1=[[abs(i1-K),i1]for i1 in [int(x1) for x1 in input().split()]]
u1.sort()
u1=u1[1:]
u1=[i1[1] for i1 in u1[:3]]
print(*u1)
