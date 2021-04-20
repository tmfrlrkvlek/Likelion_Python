# 은행의 기능들을 모아놓은 python 파일입니다.
from .account import Account                         

accountList = []                            # 개설된 계좌 모음

def printMenu() :                           # BankMenu 출력하기
    print("======Bank Menu======")
    print("1. 계좌개설")
    print("2. 입금하기")
    print("3. 출금하기")
    print("4. 이체하기")
    print("5. 전체조회")
    print("6. 통장해지")
    print("7. 종료하기")
    print("=====================")

def doFunc(order) :                         # 은행의 각 기능들로 연결
    if order == 1 :                         # 계좌개설
        makeAccount()
    elif order == 2 :                       # 입금하기
        deposit()                 
    elif order == 3 :                       # 출금하기
        withdraw()
    elif order == 4 :                       # 이체하기
        transfer()
    elif order == 5 :                       # 전체조회
        checkList()
    elif order == 6 :                       # 통장해지
        removeAccount()
    elif order == 7 :                       # 종료하기
        return 0
    else :
        print("##잘못 입력하셨습니다##")
    return 1

def makeAccount():                          # 계좌개설
    print("======계좌개설======")
    accountNum = int(input("계좌번호 : "))
    while findCustomer(accountNum, 0) :     # 예외 - 계좌번호 중복 체크
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

def deposit():                              # 입금하기
    print("======입금하기======")
    accountNum = int(input("입금하실 계좌번호를 입력해주세요 : "))
    account = findCustomer(accountNum, 0)
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
    account = findCustomer(accountNum, 0)
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

def transfer():
    print("======이체하기======")
    accountNum = int(input("출금하실 계좌번호를 입력해주세요 : "))
    accountTo = findCustomer(accountNum, 0)
    if accountTo:
        accountNum = int(input("이체하실 계좌번호를 입력해주세요 : "))
        accountFrom = findCustomer(accountNum, 0)
        if accountFrom:
            checkAccount(accountTo)
            money = int(input("이체하실 금액을 입력해주세요 : "))
            while checkMinus(money, "이체하실"):
                money = int(input("이체하실 금액을 입력해주세요 : "))
            accountTo.real_withdraw(money)
            accountFrom.real_deposit(money)
            checkAccount(accountTo)
        else :
            print("##존재하지 않는 계좌번호입니다##")
    else :
        print("##존재하지 않는 계좌번호입니다##")
    print("==================")

def checkList():                            # 전체조회
    print("======전체조회======")
    if accountList:                             
        for account in accountList:
            checkAccount(account)
    else:
        print("##개설된 계좌가 존재하지 않습니다##")
    print("==================")

def removeAccount():                        # 통장해지
    print("======통장해지======")
    accountNumTo = int(input("해지하실 계좌번호를 입력해주세요 : "))
    account = findCustomer(accountNumTo, 0)
    if account:
        checkAccount(account)
        print("====Transfer Menu====")
        print("1. 이체하기")
        print("2. 출금하기")
        print("=====================")
        order = int(input("통장 잔액 처리 방법 : "))
        if order == 1:
            accountNumFrom = int(input("이체하실 계좌번호를 입력해주세요 : "))
            accountFrom = findCustomer(accountNumFrom, 0)
            if accountFrom == account :
                print("##해지 예정 계좌로 이체할 수 없습니다##")
            elif accountFrom:
                money = account.money
                accountFrom.real_deposit(money)
                findCustomer(accountNumTo, 1)
                print("##이체 후 통장해지를 완료하였습니다##")
            else :
                print("##존재하지 않는 계좌번호입니다##")
        elif order == 2:
            money = account.money
            print("##%d원이 출금되었습니다##" %money)
            findCustomer(accountNumTo, 1)
            print("##출금 후 통장해지를 완료하였습니다##")
        else: 
            print("##잘못 입력하셨습니다##")
    else :
        print("##존재하지 않는 계좌번호입니다##")
    print("==================")


def checkAccount(account):                  # 계좌조회
    print("계좌번호 : ", str(account.account), end=" / ")
    print("이름 : ", account.name, end=" / ")
    print("잔액 : ", str(account.money))

def findCustomer(accountNum, isDel):        # 계좌번호가 일치하는 계좌 찾기
    for i in range(len(accountList)):
        if accountNum == accountList[i].account :   
            if isDel :                      # 계좌 삭제
                del accountList[i]
                return 1
            return accountList[i]           # 계좌 찾기
    return 0

def checkMinus(money, message) :            # 예외 - 입력한 금액이 음수인 경우
    if money < 0:
        print("##" + message + " 금액을 다시 입력해주세요##")
        return 1
    else :
        return 0
