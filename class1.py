#class1.py
#클래스 정의
class person:
    #클래스에 소속된 멤버변수(주로 데이터를 공유) static 키워드 추가
    num_person = 0
    def __init__(self):
        #인스턴스 멤버 변수는 여기에서 초기화
        self.name = "default name"
        person.num_person += 1
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1 = person()
p2 = person()
p3 = person()
print("인스턴스갯수 : {0}".format(person.num_person))

#런타임(실행시간)시에 멤버 변수 추가 (동적 언어는 가능)
#디자인타임(코딩, 개발...)
person.title = "new title"
print(person.title)
print(p1.title)
print(p2.title)
