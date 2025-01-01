# 점수를 입력받는다.
score_str = input("점수를 입력하세요: ")

# 점수를 정수형으로 변환
score = int(score_str)

# 점수가 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 60점 이상이면 D, 그렇지 않으면 F
# if score > 99 or score < 1:
#     print("점수를 다시 입력하세요.")
# elif score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("F")

if score <=99 and score >=90:
  grade = "A"
elif score <=89 and score >=80:
  grade = "B"
elif score <=79 and score >=70:
  grade = "C"
elif score <=69 and score >=1:
  grade = "F"
else:
  grade = "None"

print(f"점수는 {score}이고, 학점은 {grade}입니다.")