n = list(map(int,input().split()))
if n[1] < 10:
    if n[2] < 10:
        print("%d0%d00%d" % (n[0], n[1], n[2]))
    elif n[2] < 1000 and n[2] >= 100:
        print("%d0%d%d" % (n[0], n[1], n[2]))
    else:
        print("%d0%d0%d" % (n[0], n[1], n[2]))
else:
    if n[2] < 10:
        print("%d%d00%d" % (n[0], n[1], n[2]))
    elif n[2] < 1000 and n[2] >= 100:
        print("%d%d%d" % (n[0], n[1], n[2]))
    else:
        print("%d%d0%d" % (n[0], n[1], n[2]))
