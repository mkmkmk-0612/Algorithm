n = list(map(int,input().split()))
if n[2] < 10:
    print("%d%d0%s"%(n[0],n[1],str(n[2])))
else:
    print("%d%d%s"%(n[0],n[1],str(n[2])))
