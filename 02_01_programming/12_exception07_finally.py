# 보통 finally절은 사용한 리소스를 close해야 할 때에 많이 사용
f = open('test.txt', 'w')
try:
    f.write("ttt")
finally:
    f.close()