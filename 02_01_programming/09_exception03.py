### 어떤 에러 메시지인지 알 수 있을까?
### Exception : 예외 발생 해당되는 에러가 없을 때 실행된다.
### Exception as e : 이 구문을 통해 에러 내용을 e를 통해 출력 가능

try:
    x = int(input('5의 배수를 입력하세요: '))
    print("내가 입력한 값 : ", x)
except Exception as e:                             # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다. \n[에러내용]', e)


