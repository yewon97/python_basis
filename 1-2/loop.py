# for loop
for i in range(10):
    print(i)

for i in range(2, 5):
    print(i)
else:
		print("반복이 완료되었습니다.")

# while loop
i = 0
while i < 10:
    print(i)
    i += 1
    
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
	if fruit == "banana":
			print("banana is found")
    
	print(fruit)

while True:
  user_input = input("명령어럴 입력해주세요: ")
  if user_input == "exit":
    break
  else:
    pass # TODO: 차후 개발

# 구구단 프로그램
# 1단 ~ 9단, n * 1 ~ n * 9
for x in range(1, 10):
    for y in range(1, 10):
        print(f"{x} * {y} = {x * y}")
