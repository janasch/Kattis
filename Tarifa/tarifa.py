import sys

cap = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
bal = 0

for _ in range(N):
    bal += cap - int(sys.stdin.readline().strip()) 

print(bal+cap)

