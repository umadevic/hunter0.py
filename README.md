y1 = list(map(int, input().split()))

t1 = list(map(int, input().split()))

t1.sort(reverse=True)

print(t1[y1[-1]-1])
