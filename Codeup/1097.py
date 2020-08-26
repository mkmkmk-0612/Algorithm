arr = [[0 for i in range(19)] for j in range(19)]
for i in range(19):
    n = list(map(int, input().split()))
    for j in range(19):
        arr[i][j] = n[j]
x = int(input())
for i in range(x):
    x, y = map(int, input().split())
    for j in range(19):
        if arr[j][y-1] == 0:
            arr[j][y-1] = 1
        else:
            arr[j][y-1] = 0

        for k in range(19):
            if arr[x-1][k] == 0:
                arr[x-1][k] = 1
            else:
                arr[x-1][k] = 0

for i in range(19):
    for j in range(19):
        print(arr[i][j], end =' ')
    print('')
