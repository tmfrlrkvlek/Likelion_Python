
class Account :
    account = 0
    name = ""
    money = 0
    
    def __init__(self, account, name, money) :      # 계좌생성
        self.account = account
        self.name = name
        self.money = money

    def real_deposit(self, money):                  # 입금
        self.money += money
    
    def real_withdraw(self, money):                 # 출금
        ### 구현할 기능 1-2 ###
        if self.money < money:
            print("##돈이 부족합니다##")
        else:
            self.money -= money