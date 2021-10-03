
# try except
# Exception 으로 에러 문 확인
try:
    print("구간1")
    a= 1/0
    print("구간2")
except Exception as e:
    print(e.__class__.__name__)
    print(e)

finally:
    print("구문 빠저나가기 전에")

print("구간3")


# 해당 error에 대한 에이징

try:
    print("구간1")
    a= 1/0
    print("구간2")
except ZeroDivisionError as e:
    print("나누기 애러")

print("구간3")