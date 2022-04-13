# 예외 발생 시키기 및 특정 오류 회피하기


# 01 raise 예외 발생
try:
    x = int(input('5의 배수를 입력하세요: '))
    if x % 5 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('5의 배수가 아닙니다.')    # 예외를 발생시킴
    print(x)
except Exception as e:                             # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.', e)

# 02 특정 오류 회피
try:
    x = int(input('5의 배수를 입력하세요: '))
    print(x)
except ValueError:            # 특정 오류 회피할때
    pass