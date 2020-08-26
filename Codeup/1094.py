n = int(input())
x = input().split()
arr = [0]*n
for i in range(n):
    arr[i] = x[i]
for i in reversed(range(n)):
    print(x[i], end = ' ')
