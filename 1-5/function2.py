# 기본 매개변수
def welcome(city, name = "Guest", room = None):
  if room is None:
    room = []
    
  room.append(101)
  print(f"{city}에 오신 것을 환영합니다. {name}님. 방은 {room}입니다.")

welcome("서울")
welcome("서울", "연탄이")
