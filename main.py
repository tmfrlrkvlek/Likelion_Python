from bank import bankFunc, account      # bank 패키지의 bankFunc.py account.py 파일 import

isContinue = 1                          # 프로그램 종료 유무 판단 변수 (1 - 진행, 0 - 종료)

while isContinue :                      # 사용자가 종료를 누르기까지 진행
    bankFunc.printMenu()
    order = int(input("입력 : "))        # 사용자의 명령 받기
    isContinue = bankFunc.doFunc(order)