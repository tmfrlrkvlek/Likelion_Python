
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
        ''' 아래 '돈이 부족하다면' 부분을 조건으로 바꾸고 기능을 완성
        if 돈이 부족하다면 : 
            print("##돈이 부족합니다##") 
        else
            self.money -= money'''