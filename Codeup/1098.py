h, w = map(int, input().split())
arr = [[0 for i in range(w)] for j in range(h)]
n = int(input())

for i in range(n):
    c = 0
    l, v, x, y = list(map(int, input().split()))
    for j in range(l):
        if v == 0:
            arr[x-1][y-1+j] = 1
        else:
           arr[x-1+j][y-1] = 1

for i in range(h):
    for j in range(w):
        print(arr[i][j], end =' ')
    print('')
