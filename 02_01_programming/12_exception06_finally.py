# finally 절은 예외와 상관없이 언제나 실행
# try:
#    실행문1
# except 발생 오류1:
#    실행문2
# except 발생 오류2:
#    실행문3
# finally:
#    실행문

try:
    3 / 0
except IndexError as e:
    print("인덱스가 안 맞습니다.", e)
except ZeroDivisionError as e:
    print("0으로 나누면 안됩니다.", e)
finally:
    print("예외에 상관없이 언제나 실행!")

print("프로그램이 정상적으로 종료됩니다!")
