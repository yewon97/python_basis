# 사용자로부터 두 개의 값을 입력받는다.
var1 = input("첫 번째 값을 입력하세요: ")
var2 = input("두 번째 값을 입력하세요: ")

# 입력값을 숫자로 변환 
num_var1 = int(var1) # 첫 번째 값을 정수형으로 변환
num_var2 = int(var2) # 두 번째 값을 정수형으로 변환

# 첫 번째 값이 크다면 "win" 출력, 두 번쨰 값이 크다면 "lose" 출력, 두 값이 같다면 "draw" 출력
if num_var1 > num_var2:
    print("win")
elif num_var1 < num_var2:
    print("lose")
else:
    print("draw")
    