import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
a, b, c = map(int, input().split())
if (a-b+c)%10==0:
    print('대박')
else:
    print('그럭저럭')
