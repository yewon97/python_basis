# 기본 매개변수
def welcome(city, name = "Guest", room = None):
  if room is None:
    room = []
    
  room.append(101)
  print(f"{city}에 오신 것을 환영합니다. {name}님. 방은 {room}입니다.")

welcome("서울")
welcome("서울", "연탄이")

# 키워드 인자
def display_info( age, city, name):
  print(f"이름: {name}, 나이: {age}, 도시: {city}")

display_info(name="연탄이", age=2, city="서울")
# 키워드 인자인 경우 순서는 상관없음

# 가변인자 리스트 (튜플)
# 매개변수는 가변인자 앞으로 작성해야함
# 만약 가변인자 뒤에 매개변수를 추가하고 싶으면 키워드 인자를 사용해야함
def calc_sum(*args):
  total = 0
  for arg in args:
    total += arg     # total = total + arg
  return total

print(calc_sum(1, 2, 3, 4, 5))
print(calc_sum(10, 100))

# 키워드 가변인자 리스트
def print_info(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_info(name="연탄이", age=30, city="서울")

info = {"name": "연탄이", "age": 30, "city": "서울"}
# 딕셔너리를 키워드 인자로 전달하기 위해서는 **를 사용해야함
print_info(**info)


