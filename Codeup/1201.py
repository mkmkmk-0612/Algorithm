import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
n = int(input())
if n<0:
    print('음수')
elif n>0:
    print('양수')
else:
    print('0')
