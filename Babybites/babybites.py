n = int(input())
i = 0
for inp in input().split():
    i += 1
    try:
        val = int(inp)
        if val != i:
            print('something is fishy')
            exit()
    except ValueError:
            continue
print('makes sense')

