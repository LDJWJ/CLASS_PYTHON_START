# 예외처리 exception 알아보기
# 내용 : 문자로 나눌 때, 이에 대한 에러 메시지 출력하기

# 기본 구조
# try:
#     ...
# except [발생 오류] [as 오류 메시지 변수]:
#     ...

def divide(a, b):
    return a/b

try:
    c = divide(5, 'string')
except ZeroDivisionError:
    print("두번째 인자는 0이어서는 안됩니다.")
except TypeError:
    print("모든 인자는 숫자여야 합니다.")
except:
    print("무슨 에러?")