import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
n = list(map(int, input().split(" ")))
n = n[0] + n[1] + n[2] + n[3]
if n == 0:
    print('모')
elif n == 1:
    print('도')
elif n == 2:
    print('개')
elif n == 3:
    print('걸')
else:
    print('윷')
