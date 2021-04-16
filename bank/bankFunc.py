from .account import Account                         ###>>> account 앞에 . 이 있는 이유는 뭔가요?

# 은행의 기능들을 모아놓은 python 파일입니다.

accountList = []                    # 개설된 계좌 모음

def printMenu() :                   # BankMenu 출력하기
    print("======Bank Menu======")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체조회")
    print("5. 종료하기")
    print("=====================")

def doFunc(order) :                 # 은행의 각 기능들로 연결
    if order == 1 :                 # 계좌개설
        makeAccount()
    elif order == 2 :               # 입금하기
        deposit()                 
    elif order == 3 :               # 출금하기
        withdraw()
    elif order == 4 :               # 전체조회
        checkList()
    elif order == 5 :
        return 0
    else :
        print("##잘못 입력하셨습니다##")
    return 1

def makeAccount():                  # 계좌개설
    print("======계좌개설======")
    accountNum = int(input("계좌번호 : "))
    name = input("이름 : ")
    money = int(input("예금 : "))
    account = Account(accountNum, name, money)    ###>>> Account라는 클래스 괄호하고 변수를 넣은 것은 무슨 뜻인가요?
    accountList.append(account)
    print("##계좌개설을 완료하였습니다##")
    print("==================")

def deposit():                      # 입금하기
    print("======입금하기======")
    accountNum = int(input("입금하실 계좌번호를 입력해주세요 : "))
    account = findCustomer(accountNum)
    if account:
        checkAccount(account)
        money = int(input("입금하실 금액을 입력해주세요 : "))
        account.real_deposit(money)               ###>>> account에 Account 클래스의 real_deposit 메소드를 실행했을 때 입금 되는 원리?
        checkAccount(account)
    print("==================")

def withdraw():                     # 출금하기
    print("======출금하기======")
    ### 구현할 기능 1 ###
    ''' 입금하기 기능 처럼 출금하기 기능 구현 
    (참고 - Account 클래스의 real_withdraw 함수 구현 및 사용) '''
    accountNum = int(input("출금하실 계좌번호를 입력해주세요 : "))
    account = findCustomer(accountNum)
    if account:
        checkAccount(account)
        money = int(input("출금하실 금액을 입력해주세요 : "))
        account.real_withdraw(money)
        checkAccount(account)
    print("==================")

def checkList():                    # 전체조회
    print("======전체조회======")
    ### 구현할 기능 2 ###
    ''' 전체 조회 기능을 구현
    (참고 - 반복문과 아래의 checkAccount 함수를 사용) '''

    if accountList:                             ###>>> 이렇게 if 문 사용해도 되나 모르겠습니다..ㅎ
        for account in accountList:
            return checkAccount(account)
    else:
        print("개설된 계좌가 존재하지 않습니다.")
    print("==================")

def checkAccount(account):                  # 계좌조회
    print("계좌번호 : ", str(account.account), end=" / ")
    print("이름 : ", account.name, end=" / ")
    print("잔액 : ", str(account.money))

def findCustomer(accountNum):               # 계좌번호가 일치하는 계좌 찾기
    for account in accountList :
        if account.account == accountNum :
            return account
    print("##존재하지 않는 계좌번호입니다##")
    return 0