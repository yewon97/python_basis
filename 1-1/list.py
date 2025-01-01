my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# my_list.append(40)

# print(len(my_list))

# print(my_list)

# element = my_list[3]
# # print('element: ', element)

# sliced = my_list[1:3]
# print('sliced: ', sliced)

# sliced = my_list[1:]
# print('sliced: ', sliced)

# sliced = my_list[:3]
# print('sliced: ', sliced)

# sliced = my_list[:]
# print('sliced: ', sliced)

# sliced = my_list[::2]
# print('sliced: ', sliced)

# sliced = my_list[::-1]
# print('sliced: ', sliced)

# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# sliced = my_list[::4]
# print('sliced: ', sliced)

# sliced = my_list[::-4]
# print('sliced: ', sliced)

# sliced = my_list[::-5]
# print('sliced: ', sliced)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'pear', 'plum', 'pomegranate', 'raspberry', 'strawberry', 'tangerine', 'watermelon']

# 바나나가 포함되어 있나요?
is_banana_in_fruits = 'banana' in fruits
print('is_banana_in_fruits: ', is_banana_in_fruits)

# 체리의 위치는?
index_of_cherry = fruits.index('cherry')
print('index_of_cherry: ', index_of_cherry)

# 리스트의 정렬
numbers = [4, 9, 2, 1, 7, 6, 8, 3, 5]
print('numbers: ', numbers)
numbers.sort() # 오름차순
print('numbers: ', numbers)
numbers.sort(reverse=True) # 내림차순
print('numbers: ', numbers)

# 리스트의 역순
numbers.reverse() # 역순
print('numbers: ', numbers)

# 리스트의 요소 추가 및 제거
my_list2 = []
my_list2.append(10)
my_list2.append(20)
my_list2.append(30)
print('my_list2: ', my_list2)

my_list2.extend([40, 50, 60])
my_list2.append([70, 80, 90])
print('my_list2: ', my_list2)

# 리스트 연산 (+, *)
# my_list3 = [1, 2, 3]
# my_list4 = [4, 5, 6]
# my_list5 = my_list3 + my_list4
# print('my_list5: ', my_list5)

# my_list6 = my_list3 * 3
# print('my_list6: ', my_list6)

# my_list2.insert(1, 15)
# print('my_list2: ', my_list2)

my_list2.remove(20)
print('my_list2 remove: ', my_list2)

del my_list2[1]
print('my_list2 del: ', my_list2)

# my_list2.pop()
# print('my_list2: ', my_list2)

# my_list2.clear()
# print('my_list2: ', my_list2)

# 최대값 & 최솟값
max_value = max(my_list)
min_value = min(my_list)
print('max_value: ', max_value)
print('min_value: ', min_value)

# 리스트 복사
my_list_copy = my_list.copy()
print('my_list_copy: ', my_list_copy)
