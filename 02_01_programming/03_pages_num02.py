# 게시물의 페이지 확인 계산 프로그램
# 내용 : 페이지 수와 마지막 페이지에 표시될 건수를 확인하는 프로그램을 만들어보기.

def NumPage(m, n):
    page = m // n+1
    last_page_num = m % n
    return page, last_page_num


m1 = int(input("총 게시물 수 : "))
n1 = int(input("한 페이지 게시물 건수 : "))

page, last_num = NumPage(m1, n1)
print()
print(f"게시물 전체 페이지 : {page} 마지막 페이지 게시물 건수 : {last_num}" )