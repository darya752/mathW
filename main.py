a, b, c, d = map(int, input().split())
e = a + b
s = c + d
if e == 180 or s == 180:
    print('да')
elif e == 180 and s == 180:
    print('да')
else:
    print('нет')
