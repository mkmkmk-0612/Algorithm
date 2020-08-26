n = int(input())
x = input().split()
arr = [0]*23
for i in range(n):
    arr[int(x[i])-1] += 1
for i in range(len(arr)):
    print(arr[i], end =' ')
