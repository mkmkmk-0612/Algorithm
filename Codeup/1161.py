import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
a, b = map(int, input().split())
c = a+b
if a%2==0:
    print('짝수+', end = '')
else:
    print('홀수+', end = '')
if b%2==0:
    print('짝수=', end = '')
else:
    print('홀수=', end = '')
if c%2==0:
    print('짝수')
else:
    print('홀수')
