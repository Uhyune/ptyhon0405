#다중 상속의 문제점
class Tiger:
    def jump(self):
        print("호랑이 점프")
    def cry(self):
        print("호랑이 어흥")

class Lion:
    def bite(self):
        print("사자 물어뜯기")
    def cry(self):
        print("사자 어흥")
#다중으로 상속을 받을 때 이름 충돌
class Liger(Lion, Tiger):
    def play(self):
        print("라이거와 놀기")

#인스턴스 생성
l = Liger()
l.cry()
print("내부에 상속에 순서 튜플:{0}".format(Liger.__mro__))

        
