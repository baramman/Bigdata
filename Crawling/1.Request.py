"""
날짜 : 2022/02/28
이름 : 양성민
내용 : 파이썬 HTML 페이지 요청 실습

# 패키지 설치 : pip3 install requests
"""

import requests as req

html = req.get('https://naver.com').text
print(html)

print('-'*20)

test = req.get('http://chhak.or.kr/test.html').text
print(test)
