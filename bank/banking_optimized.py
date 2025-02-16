import random
from abc import ABC, abstractmethod

class BankUser:
    def __init__(self, name, money):
        self.__accounts = []
        self.__name = name
        self.__money = money

    def get_name(self):
        return self.__name

    def get_money(self):
        return self.__money

    def get_accounts(self):
        for account in self.__accounts:
            account.info()

    def get_assets(self):
        print(f"이름: {self.__name}, 보유 현금: ${self.__money}")
        self.get_accounts()

    def open_account(self, account_type, amount, **kwargs):
        """계좌 개설과 동시에 자금 이동"""
        if self.__money < amount:
            print("잔액 부족으로 계좌 개설이 불가능합니다.")
            return None
        
        self.__money -= amount

        if account_type == "checking":
            account = CheckingAccount(self.__name, amount, kwargs.get("withdraw_limit", 500))
        elif account_type == "savings":
            account = SavingsAccount(self.__name, amount, kwargs.get("interest_rate", 0.05))
        else:
            print("잘못된 계좌 타입입니다.")
            return None

        self.__accounts.append(account)
        return account

    def transfer(self, from_account, to_account, amount):
        """계좌 간 이체"""
        if from_account.withdraw(amount):
            to_account.deposit(amount)
            print(f"${amount} 이체 완료: {from_account.get_account_number()} -> {to_account.get_account_number()}")
        else:
            print("이체 실패: 잔액 부족")

    def transfer_with_limit(self, account, amount):
        """출금 한도 초과 시 한도 조정 후 재출금"""
        if not account.withdraw(amount):
            account.update_limit(amount)
            account.withdraw(amount)
        self.add_money(amount)

    def add_money(self, amount):
        self.__money += amount

class BankAccount(ABC):
    def __init__(self, holder_name, balance):
        self._account_number = random.randint(10000000, 99999999)
        self._holder_name = holder_name
        self.__balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("출금 실패: 잔액 부족")
            return False
        else:
            self.__balance -= amount
            return True

    @abstractmethod
    def info(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self, holder_name, balance, interest_rate):
        super().__init__(holder_name, balance)
        self.__interest_rate = interest_rate
        self.__is_locked = True

    def withdraw(self, amount):
        if self.__is_locked:
            print("출금 실패: 계좌가 잠겨 있습니다.")
            return False
        return super().withdraw(amount)

    def info(self):
        print(f"[예금/{self.get_account_number()}] {self._holder_name}님 잔액 ${self.get_balance()}, "
              f"이자율 {self.__interest_rate * 100}%, 출금 제한 여부: {self.__is_locked}")

    def unlock(self):
        self.__is_locked = False
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)

class CheckingAccount(BankAccount):
    def __init__(self, holder_name, balance, withdraw_limit=500):
        super().__init__(holder_name, balance)
        self.__withdraw_limit = withdraw_limit

    def update_limit(self, new_limit):
        self.__withdraw_limit = new_limit

    def withdraw(self, amount):
        if amount > self.__withdraw_limit:
            print("출금 실패: 출금 한도 초과")
            return False
        return super().withdraw(amount)

    def info(self):
        print(f"[입출금/{self.get_account_number()}] {self._holder_name}님 잔액 ${self.get_balance()}, "
              f"출금 한도 ${self.__withdraw_limit}")