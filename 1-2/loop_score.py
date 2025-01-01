students = {} # 학생 정보 dictionary 구조로 저장

# 입력대기창
while True:
  print("")
  # 메뉴 출력
  print("1. 성적 입력하기")
  print("2. 학생 조회하기")
  print("3. 학점 조회하기")
  print("0. 종료하기")
  menu = input("메뉴를 선택해주세요: ")
  
  # 1. 성적 입력하기
  if menu == "1":
    student_name = input("학생 이름을 입력해주세요: ")
    score = input("성적을 입력해주세요: ")
    students[student_name] = int(score)
    print(f"{student_name} 학생의 성적은 {students[student_name]} 입니다.")
  
  # 2. 학생 조회하기
  elif menu == "2":
    student_name = input("학생 이름을 입력해주세요: ")
    if student_name in students.keys():
      print(f"{student_name} 학생의 성적은 {students[student_name]} 입니다.")
    else:
      print(f"{student_name} 학생은 등록되지 않았습니다.")
      
  # 3. 학점 조회하기
  elif menu == "3":
    student_name = input("조회하고자 하는 학생 이름을 입력해주세요: ")
    
    if student_name not in students.keys():
      print(f"{student_name} 학생은 등록되지 않았습니다.")
      continue
    
    score = students[student_name]
    if score <= 99 and score >= 90:
      grade = "A"
    elif score <= 89 and score >= 80:
      grade = "B"
    elif score <= 79 and score >= 70:
      grade = "C"
    elif score <= 69 and score >= 60:
      grade = "D"
    elif score <= 59 and score >= 1:
      grade = "F"
    else:
      grade = None
      
    if grade in ["A", "B", "C", "D"]:
      mod = score % 10
      if mod >= 5:
        grade = grade + "+"
    
    print(f"{student_name} 학생의 학점은 {grade}입니다.")
          
  # 4. 종료하기
  elif menu == "0":
    print("프로그램을 종료합니다.")
    break
  
  else:
    print("잘못된 메뉴를 선택하였습니다.")
