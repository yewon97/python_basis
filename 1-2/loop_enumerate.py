# enumerate
for i, value in enumerate(["apple", "banana", "cherry"]):
    print(i, value)

for i, value in enumerate(["apple", "banana", "cherry"], start=1):
    print(i, value)
    
# 팩토리얼 구하기
# n! = n * (n-1) * (n-2) * ... * 1
num = 10
result = 1

for i in range(1, num + 1):
  result = result * i
  
print(f"{num}! = {result}")