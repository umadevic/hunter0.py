p1 = list(map(int, input().split()))
o1 = list(map(int, input().split()))
o1.sort(reverse=True)
print(o1[p1[-1]-1])
