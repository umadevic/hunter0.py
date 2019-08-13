y1 = list(map(int, input().split()))
u1 = list(map(int, input().split()))
u1.sort(reverse=True)
print(u1[y1[-1]-1])
