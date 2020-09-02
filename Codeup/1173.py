m,n = input().split()
m = int(m)
n = int(n)

if n<30:
    if m == 0:
        m = 23
    else:
        m = m - 1
    n = 60 - 30 + n
else:
    n = n - 30

print(m ,n)
