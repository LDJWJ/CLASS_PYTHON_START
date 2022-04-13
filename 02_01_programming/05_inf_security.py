# 정보의 암호화 하기 - 일반적 방법

# 사전 확인
# 문자열.isdigit() : 숫자인지 확인하는 함수
# 리스트.append() : 숫자인지 확인하는 함수

## 정보
data = """
park,10234-1422351
lim ,22342-1422251
"""

##
result = []
for line in data.split("\n"):  # 한줄 단위로 구분
    word_result = []

    one_line = line.split(",")  # 한줄 데이터를 공백으로 나누기
    for word in one_line:
        if len(word) == 13 and word[:5].isdigit() and word[6:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))
