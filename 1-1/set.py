empty_set = set()
my_set = {1, 2, 3, 3, 4, 5} # 중복 허용 X

print('empty_set: ', empty_set)
print('my_set: ', my_set)

# empty_set = {} # 빈 딕셔너리
# empty_set = [] # 빈 리스트
# empty_set = () # 빈 튜플

fruits = {'apple', 'banana', 'cherry'}
print('fruits: ', fruits)

fruits.add('fig') # 요소가 순서대로 추가되지 X
print('fruits add: ', fruits)

fruits.remove('banana')
print('fruits remove: ', fruits)


fruits1 = {'apple', 'banana', 'cherry'}
fruits2 = {'banana', 'orange', 'peach'}

# 합집합
print('union :', fruits1.union(fruits2))
print('union :', fruits1 | fruits2)

# 교집합
print('intersection', fruits1.intersection(fruits2))
print('intersection', fruits1 & fruits2)

# 차집합 (순서 중요)
print('difference 1 - 2', fruits1.difference(fruits2))
print('difference 2 - 1', fruits2.difference(fruits1))
print('difference 1 - 2', fruits1 - fruits2)
print('difference 2 - 1', fruits2 - fruits1)

# 대칭차집합
# print('symmetric_difference', fruits1.symmetric_difference(fruits2))
# print('symmetric_difference', fruits1 ^ fruits2)