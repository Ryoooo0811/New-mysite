t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))
print(t[0])
print(t[1])
print(t[-1])
print(t[2:5])
print(t.index(1))
print(t.index(1, 1))
print(t.count(1))
# タプルはリストと違い、値を変更することはできない。読み取り専用。
print('\n')

t = ([1, 2, 3], [4, 5, 6])
t[0][0] = 100
t = 1, 2, 3
print(type(t))