empty_tuple = ()
single_tuple = (1,)
multiple_tuple = (1, 2, 3)

print('empty_tuple: ', empty_tuple)
print('single_tuple: ', single_tuple)
print('multiple_tuple: ', multiple_tuple)

# 튜플 생성
tp = 1, 2, 3, 4, 5
print('tp: ', tp)

# 튜플 언팩
(x, y, z, *rest) = tp
print('x: ', x)
print('y: ', y)
print('z: ', z)
print('rest: ', rest)
print(f"{x}, {y}, {z}, {rest}")

a, _, c, *vals = tp
print('a: ', a)
print('c: ', c)
print('vals: ', vals)

tuple_data = 10, 20
t, p = tuple_data
t, p = p, t
print('t: ', t)
print('p: ', p)

# 과일 바구니
fruits = ('apple', 'banana', 'cherry', 'date', 'elderberry')
print('fruits: ', fruits)
first = fruits[0]
print('first: ', first)
last = fruits[-1]
print('last: ', last)

