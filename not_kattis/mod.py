R = int(input()) #range
x, y, z = [int(x) for x in input().split()]

N = x + y*R + z*R*R

print(N)

print(x, N%R)
print(y, int((N/R)%R))
print(z, int(N/ (R*R)))
