while True:
  try:
    num1 = int(input("첫번째 숫자를 입력해주세요: "))
    num2 = int(input("두번째 숫자를 입력해주세요: "))
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
    break
  except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
    continue
  except ValueError:
    print("숫자를 입력해주세요.")
    continue
  except:
    pass