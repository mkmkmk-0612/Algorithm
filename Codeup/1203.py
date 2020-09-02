import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

n = int(input())
if n<=10:
    print('정상')
elif n>10 and n<=20:
    print('과체중')
else:
    print('비만')
