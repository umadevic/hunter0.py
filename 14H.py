from itertools import permutations
u2=input()
p=permutations(u2)
for i in list(p):
    print("".join(i))
