from banking_optimized import BankUser

# 사용자 생성
user1 = BankUser("Amy", 1000)

# 입출금 계좌 개설 (200 USD 입금)
checking_account = user1.open_account("checking", 200)

# 예금 계좌 개설 (800 USD 입금)
savings_account = user1.open_account("savings", 800, interest_rate=0.05)

# 예금 계좌 만기 후 400 USD 출금하여 입출금 계좌로 이체
savings_account.unlock()
user1.transfer(savings_account, checking_account, 400)

# 보유 자산 조회
user1.get_assets()

# ------------------------------------------------------------

# 고객 B는 $900 잔액 보유
user2 = BankUser("Bob", 900)

# 고객 B는 입출금 계좌에 $800 저축
checking_account = user2.open_account("checking", 800)

# 고객 B는 예금 계좌에 $100을 저축, 이율은 6%
savings_account = user2.open_account("savings", 100, interest_rate=0.06)

# 고객 B는 입출금 계좌에서 $800 출금하려 하지만, 출금한도에 걸려 출금 실패
if not checking_account.withdraw(800):
    checking_account.update_limit(800)  # 한도 조정
    checking_account.withdraw(800)

# 출금된 800달러를 보유 현금에 추가
user2.add_money(800)

# 보유한 현금과 계좌 목록을 출력한다.
user2.get_assets()
