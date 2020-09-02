a, b= map(str, input().split())
if b=='1' or b=='2':
    print(12+100-int(a[:2])+1)
elif b=='3' or b=='4':
    print(12-int(a[:2])+1)
