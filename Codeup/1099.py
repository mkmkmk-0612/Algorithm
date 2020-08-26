arr = []
for i in range(10):
    x = list(map(int, input().split()))
    arr.append(x)
start_x = 1
start_y = 1
while True:
    if arr[start_x][start_y] == 0:
        arr[start_x][start_y] = 9
    elif arr[start_x][start_y] == 2:
        arr[start_x][start_y] = 9
        break
    if arr[start_x][start_y+1] == 1 and arr[start_x+1][start_y]==1:
        break
    if arr[start_x][start_y+1] != 1:
        start_y += 1
    elif arr[start_x+1][start_y] != 1:
        start_x += 1
for i in range(10):
    for j in range(10):
        print(arr[i][j], end=' ')
    print()
