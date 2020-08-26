n, m ,k = map(int, input().split())
count = 0
for i in range(n):
    for j in range(m):
        for s in range(k):
            print(i, j, s)
            count += 1
print(count)
