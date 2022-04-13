### else절
# 예외가 발생하지 않았을 때, 실행되는 부분

try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('입장 가능합니다.')