# 은행의 기능들을 모아놓은 python 파일입니다.
from .account import Account                         

accountList = []                            # 개설된 계좌 모음

def printMenu() :                           # BankMenu 출력하기
    print("======Bank Menu======")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 전체조회")
    print("5. 계좌삭제")
    print("6. 종료하기")
    print("=====================")

def doFunc(order) :                         # 은행의 각 기능들로 연결
    if order == 1 :                         # 계좌개설
        makeAccount()
    elif order == 2 :                       # 입금하기
        deposit()                 
    elif order == 3 :                       # 출금하기
        withdraw()
    elif order == 4 :                       # 전체조회
        checkList()
    elif order == 5 :
        deleteAccount()
    elif order == 6 :
        return 0
    else :
        print("##잘못 입력하셨습니다##")
    return 1

def makeAccount():                          # 계좌개설
    print("======계좌개설======")
    accountNum = int(input("계좌번호 : "))
    while findCustomer(accountNum) :        # 예외 - 계좌번호 중복 체크
        print("##이미 등록된 계좌번호 입니다##")
        accountNum = int(input("계좌번호 : "))
    name = input("이름 : ")
    money = int(input("예금 : "))
    while checkMinus(money, "예금하실"):
        money = int(input("예금 : "))
    account = Account(accountNum, name, money)    
    accountList.append(account)
    print("##계좌개설을 완료하였습니다##")
    print("==================")

def deleteAccount():
    print("======계좌삭제======")
    accountNum = int(input("삭제할 계좌번호를 입력해주세요 : "))
    account = findCustomer(accountNum)
    if account :
        checkAccount(account)
        check_last = int(input("위 계좌를 진짜 삭제하시려면 1을 입력해주세요 : "))
        if check_last == 1 :
            accountList.remove(account)
            print("##계좌삭제를 완료하였습니다##")
        # else :
        #     pass
    else :
        print("##존재하지 않는 계좌번호입니다##")       
    print("==================")

def deposit():                              # 입금하기
    print("======입금하기======")
    accountNum = int(input("입금하실 계좌번호를 입력해주세요 : "))
    account = findCustomer(accountNum)
    if account:
        checkAccount(account)
        money = int(input("입금하실 금액을 입력해주세요 : "))
        while checkMinus(money, "입금하실"):
            money = int(input("입금하실 금액을 입력해주세요 : "))
        account.real_deposit(money)
        checkAccount(account)
    else :
        print("##존재하지 않는 계좌번호입니다##")
    print("==================")

def withdraw():                             # 출금하기
    print("======출금하기======")
    accountNum = int(input("출금하실 계좌번호를 입력해주세요 : "))
    account = findCustomer(accountNum)
    if account:
        checkAccount(account)
        money = int(input("출금하실 금액을 입력해주세요 : "))
        while checkMinus(money, "출금하실"):
            money = int(input("출금하실 금액을 입력해주세요 : "))
        account.real_withdraw(money)
        checkAccount(account)
    else :
        print("##존재하지 않는 계좌번호입니다##")
    print("==================")

def checkList():                            # 전체조회
    print("======전체조회======")
    if accountList:                             
        for account in accountList:
            checkAccount(account)
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
    return 0

def checkMinus(money, message) :            # 예외 - 입력한 금액이 음수인 경우
    if money < 0:
        print("##" + message + " 금액을 다시 입력해주세요##")
        return 1
    else :
        return 0
