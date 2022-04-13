# 정보의 암호화 하기 - 정규 표현식

import re

data = """
park 681120-1422351
lim  810121-1422251
"""

#
#
pat = re.compile("(\d{5})[-]\d{7}")  # 숫자 5개, 숫자 7개
print(pat.sub("\g<1>-*******", data))