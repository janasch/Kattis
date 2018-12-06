n = int(input())
c = 0
for t in [int(x) for x in input().split()]:
    if t<0:
        c += 1
print(c)
