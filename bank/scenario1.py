from account import SavingsAccount, CheckingAccount
from user import BankUser

user1 = BankUser("Amy", 1000)

# 입출금 계좌에 $200 입금
user1.deduct_money(200)
account1 = CheckingAccount(user1.get_name(), 200)
user1.add_account(account1)	

# $800 예금 계좌에
user1.deduct_money(800)
account2 = SavingsAccount(user1.get_name(), 800, 0.05)
user1.add_account(account2)

# 예금 계좌 만기 이후, 예금 계좌에서 $400 출금 후 입출금 계좌로 입금한다.
account2.unlock()
account2.withdraw(400)
user1.add_money(400)

user1.deduct_money(400)
account1.deposit(400)

# 보유한 현금과 계좌 목록을 출력한다.
user1.get_assets()


