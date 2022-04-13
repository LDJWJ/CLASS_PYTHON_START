# 하위 디렉터리 검색 후, 원하는 파일 형태만 출력
# 내용 : 확장자가 html인 파일만 출력시켜보기

import os

# 확인하고자 하는 대상 폴더
test_path = "D:\Github\CLASS_PYTHON_START"

for (path, dir, files) in os.walk(test_path):
    for filename in files:
        ext = os.path.splitext(filename)[-1]  # 경로와 확장자로 구분
        if ext=='.html':   # 확장자명
            print("%s%s" % (path, filename))