n = int(input())
year = 2012
b = year - n + 1
if b < 2000:
    if b - 1910 < 0:
        print(str(b)[3:], 1)
    else:
        print(str(b)[2:], 1)
else:
    if b - 2010 < 0:
        print(str(b)[3:], 3)
    else:
        print(str(b)[2:], 3)
