import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
a, b = input().split()
a = float(a)
b = float(b)
c = (a-100)*0.9
bmi = (b-c)*100/c
if bmi<=10:
    print('정상')
elif bmi>10 and bmi<=20:
    print('과체중')
else:
    print('비만')
