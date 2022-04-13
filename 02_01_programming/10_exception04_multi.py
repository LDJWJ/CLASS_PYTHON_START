# 다중 except

try:
    3 / 0
except IndexError as e:
    print("인덱스가 안 맞습니다.", e)
except ZeroDivisionError as e:
    print("0으로 나누면 안됩니다.", e)

print("프로그램의 정상 종료!")