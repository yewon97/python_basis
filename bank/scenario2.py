from account import CheckingAccount, SavingsAccount
from user import BankUser

# 고객 B는 $900 잔액 보유
user2 = BankUser("Bob", 900)

# 고객 B는 입출금 계좌에 $800 저축
user2.deduct_money(800)
account1 = CheckingAccount(user2.get_name(), 800)
user2.add_account(account1)

# 고객 B는 예금 계좌에 $100을 저축, 이율은 6%
user2.deduct_money(100)
account2 = SavingsAccount(user2.get_name(), 100, 0.06)
user2.add_account(account2)

# 고객 B는 입출금 계좌에서 $800를 출금하려 하지만, 출금한도에 걸려 출금 실패
try:
  account1.withdraw(800)
except ValueError:
  account1.update_limit(800)
  account1.withdraw(800)
finally:
  user2.add_money(800)

# 보유한 현금과 계좌 목록을 출력한다.
user2.get_assets()


