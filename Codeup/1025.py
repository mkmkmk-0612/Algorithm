n = input()
for i in range(len(n)):
    print('['+str(int(n[i])*10**(4-i))+"]")
