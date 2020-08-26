c = int(input(),16)
n = hex(c)[2:].upper()
for i in range(1, 16):
    print(n+"*"+hex(i)[2:].upper()+"="+hex(c*i)[2:].upper())
