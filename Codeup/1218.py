import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
n = list(map(int, input().split(' ')))
if n[0] + n[1] > n[2]:
    if (n[0] == n[1]) and (n[1] == n[2]):
        print('정삼각형')
    elif (n[0] == n[1]) or (n[1] == n[2]) or (n[0] == n[2]):
        print('이등변삼각형')
    elif n[2]**2 == n[1]**2 + n[0]**2:
        print('직각삼각형')
    else:
        print('삼각형')
else:
    print('삼각형아님')
