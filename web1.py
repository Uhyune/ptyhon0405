#web1.py
#from 패키지명 import 모듈명
from bs4 import BeautifulSoup

#페이지를 로딩(HTML문서를 읽어오기 (rt,read) 유니코드)
page = open("c:\\work2\\test01.html","rt",encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page,"html.parser")
# print(soup.prettify())
#<p>를 모두 검색 리스트 형식 리턴
# print(soup.find_all("p"))
#첫번째<p>를 검색
# print(soup.find("p"))
#<p class="outer-text"> 된 경우 (약간의 필터링)
#print(soup.find_all("p",class_="outer-text")) #class는 예약어라 _붙여서 피함
#특정 id 속성을 검색
#print(soup.find(id="first"))
#<a>태그 가져오기
#print(soup.find_all("b"))

#태그를 제거하고 내부 문자열(컨텐츠만)
#<p>컨텐츠</p>
for tag in soup.find_all("p"):
    #앞 뒤에 공백문자 제거
    print(tag.text.strip())
