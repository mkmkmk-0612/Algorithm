op = ['+', '-', '*', '/']
i = 0
k = 0
n = input()
for j in range(len(n)):
    for z in range(len(op)):
        if n[j] == op[z]:
            i = z
            k = j
if op[i] == '+':
    print(int(n[:k]) + int(n[k+1:]))
elif op[i] == '-':
    print(int(n[:k]) - int(n[k+1:]))
elif op[i] == '*':
    print(int(n[:k]) * int(n[k+1:]))
elif op[i] == '/':
    print('%.2f'%(int(n[:k]) / int(n[k+1:])))
