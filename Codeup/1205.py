a, b = input().split()
a = int(a)
b = int(b)
l = []
p = a+b
p_ = b+a
m = a-b
m_ = b-a
mul = a*b
div = a/b
div_ = b/a
z = a**b
z_ = b**a
l.append(p)
l.append(p_)
l.append(m)
l.append(m_)
l.append(mul)
l.append(div)
l.append(div_)
l.append(z)
l.append(z_)
print('%.6f'%max(l))
