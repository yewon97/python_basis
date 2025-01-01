# ToDoList를 어떻게 저장할 것인가?
# List를 저장공간으로 사용!

todo_list = []

while True:
	print("")
	print("할 일 목록 관리자")
	print("1. 할 일 추가")
	print("2. 할 일 삭제")
	print("3. 할 일 목록 조회")
	print("4. 종료")
	
	choice = input("원하는 작업을 선택하세요: ")
	
	if choice == '1':
		todo = input("추가할 일 :")
		todo_list.append(todo)
		print(f"{todo} 할 일이 추가되었습니다.")
	elif choice == '2':
		todo = input("삭제할 일 :")
		todo_list.remove(todo)
		print(f"{todo} 할 일이 삭제되었습니다.")
	elif choice == '3':
		print("할 일 목록: ", todo_list)
	elif choice == '4':
		print("프로그램을 종료합니다.")
		break
	else:
		print("잘못된 입력입니다. 다시 시도해주세요.")
	

