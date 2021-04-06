# DemoFuntion2.py
#가변인자로 덧셈처리
def varAdd(*ar):
    result = 0
    for item in ar:
        result += item
    return result

#호출
print( varAdd(2,3))
print( varAdd(2,3,4))

#함수를 정의 (단일값 스칼라)
def add10(i):
    return i + 10

x = [1,2,3,4,5]
#각 아이템에 맵핑하는 함수
#map(함수명, 순회가능한 형식)
for item in map(add10,x):
    print(item)

print("===람다 함수 사용 ===")
for item in map(lambda i:i+10,x):
    print(item)    