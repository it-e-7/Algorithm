# [10820] 문자열분석
# islower(), isupper(), isdigit(), isspace()
# EOFError : 더이상 입력값이 없는 상황
"""
이 문제에서는 입력값의 개수가 정해지지 않음 -> 예외처리 필요 
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
"""
while True:
    try:
        text = input()
        lower = sum(i.islower() for i in text)
        upper = sum(i.isupper() for i in text)
        number = sum(i.isdigit() for i in text)
        blank = sum(i.isspace() for i in text)
        print(lower, upper, number, blank)

    except EOFError:
        break
