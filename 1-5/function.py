def func():
    print("Hello")

func()

def func2(name):
    print(f"안녕하세요, {name}님")

func2("연탄이")

def sum(num1, num2):
    return num1 + num2

result_sum = sum(1, 2)
print(result_sum)

def div(num1, num2):
  if num2 == 0:
    return "0으로 나눌 수 없습니다."
  else:
    return num1 / num2

result_div = div(1, 2)
result_div2 = div(1, 0)
print(result_div)
print(result_div2)
