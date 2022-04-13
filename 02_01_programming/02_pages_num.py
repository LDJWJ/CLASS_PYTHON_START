# 게시물의 페이지 확인 계산 프로그램
# 한 페이지에 표시할 수 있는 게시물을 입력했을 때, 게시물 페이지는 얼마인가?

def NumPage(m, n):
    return m // n+1


contents = 5  # 현재 게시물 수
one_page = 10 # 한 페이지 표시 가능 건수

print( NumPage(contents, one_page), "페이지에 표시됩니다.")   # 5건, 표시할 건수 10

contents = 45  # 현재 게시물 수
one_page = 10  # 한 페이지 표시 가능 건수

print( NumPage(contents, one_page), "페이지에 표시됩니다.")   # 5건, 표시할 건수 10