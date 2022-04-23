# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:32:33 2019

3장 본문의 모든 코드
@author: Kang Hwan Soo
"""
#%% 3장 1절

#%% 문자열을 길이 
str = 'python'
len(a)
len('파이썬')

#%% 문자 참조 인덱싱 
'python'[0]
'python'[3]
'python'[-1]
'python'[len('python')-1]
'python'[-4]

'python'[6] #오류
'python'[-7] #오류

#%% 03-01strindex.py	첨자로 문자열의 문자 참조
str = 'Hello python!'
n = len(str)
print('문자열', str, '길이', n)
print('첫 문자', str[0], str[-n] )
print('가운데 문자', str[n//2], str[-n//2] )
print('마지막 문자', str[n-1], str[-1])

#%% 0, 양수 문자열 슬라이싱(string slicing)
'python'[1:5]
'python'[2:4]
'python'[0:3]
'python'[0:6]
'python'[0:len('python')]

#%% 음수 문자열 슬라이싱(string slicing)
'python'[-5:-1]
'python'[-4:-1]
'python'[-6:-3]
'python'[-6:-1]
'python'[-len('python'):-1]

#%% 음수와 0, 양수를 혼합해서 사용 가능
'python'[1:-1]
'python'[0:-2]
'python'[0:-1]
'python'[2:-2]
'python'[-5:5]
'python'[-6:4]
'python'[-4:6]

#%% 빈 문자열 ‘’을 반환
'python'[5:-1]
'python'[3:1]
'python'[-3:-4]
'python'[-3:-0]

#%% start와 end를 비우면, 각각 ‘처음부터’와 ‘끝까지’를 의미
'python'[:3]
'python'[:6]
'python'[1:]
'python'[4:]
'python'[:] #전체 반환

#%% start와 end 비우기
'python'[:3]
'python'[:4]

'python'[1:]
'python'[3:]

'python'[:]

#%% 03-02strslicing.py	슬라이싱으로 문자열의 부분 문자열 참조
str = 'Monty Python'
len(str)
str[0:5], str[6:], str[6:12]
str[-12:-7], str[-6:], str[-6:0] 

#%% step도 가능
'python'[::1]
'python'[1:5:2]
'python'[1:5:3]

#%% 음수 step도 가능
'python'[::-1]  #역순의 문자열을 반환
'python'[5:0:-1]
'python'[-1:-7:-1]

#%% 03-03strstep.py	다양한 문자열 슬라이싱
str = '일요일 기러기'
print(str[:3], str[4:]) #양수 이용
print(str[:-4], str[-3:]) #음수 이용
print(str[:], str[::], str[::1] ) #모든 문자열 참조
print(str[::2]) # 한 문자씩 건너 뛰기
print(str[::3]) # 두 문자씩 건너 뛰기
print(str[::-2]) # 역순으로 한 문자씩 건너 뛰기
print(str[::-1]) # 역순으로 출력

#%% 문자 처리
ord('가') #44032
chr(44032) #'가'
hex(ord('가')) #44032의 16진수 ac00
hex(ord('횧'))

#%%  이스케이프 시퀀스 문자
'\\' #backslash
print('\\')
'\'' #single-quote
'\"' #double quote
'\a' #bell alert sounds
'\b' #backspace(BS) removes previous character
print("ab" + "\b" + "c")
'\n' #newline
print("hello\nworld")
'\N{DAGGER}' #Prints a character from the Unicode database	print u"\N{DAGGER}"
print('\N{REMINDER RIBBON}')
'\r' #carriage return(CR). 
print("123456\rXX_XX") #XX_XX6
'a\tb'
print('a\tb')	#ASCII horizontal tab(TAB).
'\uac00' #unicode '가'
"\u041b" #unicode 'Л'
print(u"\u00D7") #×
print(u"\U0000AC00") #가 \Uxxxxxxxx	Prints 32-bit hex value Unicode character	
'\043' #rints character based on its octal value	print "\043"	#
'\xff' #Prints character based on its hex value	print "\x23"	#

#%%
str = '\'파이썬\'은 강력한 언어이다.'
print(str)
print("\"파이썬\"은 '자바'보다 코드의 양이 많이 줄어든다.")

#%% 내장 함수 min(), max()
min('ipython')
max('ipython')
min('3259')
max('3259')
min(3, 96.4, 13)
max(3, 96.4, 13)
min('ipython', 'java')
max('ipython', 'java')

#%% 중간점검 1, 03-chk01.py 
print(ord('D') - ord("A"))
print(min('java'), max('java'))
print(len('python') - len('java'))
print(len('ab\td'))
print('abc\bd')

#%% 중간점검 2, 03-chk02.py 
print('Hello_python'[5])
print('Hello_python'[:5])
print('Hello_python'[6:])
print('Hello_python'[::2])
print('Hello_python'[:len('Hello_python')])

#%% 3장 2절 

#%% 문자열 대체함수 replace()
str = '자바는 인기있는 언어 중의 하나다.'
str.replace('자바는', '파이썬은')
str.replace(' ', '')

#%% 문자열 대체함수 replace()
str = '파이썬 파이썬 파이썬'
str.replace('파이썬', 'Python!')
str.replace('파이썬', 'Python!', 1)
str.replace('파이썬', 'Python!', 2)

#%% 03-04digitsum.py	실수의 모든 자릿수 더하기 
value = input('실수(3자리.2자리로 345.78처럼)를 하나 입력하세요. >> ')
#value = '345.34'
num = value.replace('.', '')

sum = 0
sum += int(num[0])
sum += int(num[1])
sum += int(num[2])
sum += int(num[3])
sum += int(num[4])
print('입력 값:', value)
print('모든 자릿수 합:', sum)

#%% 문자열 출현횟수 count()
str = '단순한 것이 복잡한 것보다 낫다.'
str.count('복잡')
str.count('것')

#%% 문자열에 문자열 삽입
num = '12345'
'->'.join(num)

#%% 문자열 찾기 메소드 find()와 index() 
str = '자바 C 파이썬 코틀린'
str.find('자바')
str.index('자바')
str.find('파이')
str.index('파이썬')
str.find('C++')
str.index('C++') #오류

#%% 문자열 역순 찾기 메소드 rfind()와 rindex() 
'python ipython'.rfind('on')
'python ipython'.rindex('py')

#%% 03-05strchange.py	문자열에 두 단어의 순서 교환과 역순
str = input('두 개의 단어를 빈 공간으로 구분하여 입력하세요. >> ')
pos = str.find(' ')
preWord = str[:pos]
postWord = str[pos+1:]
print(preWord + postWord) 
print(preWord[::-1] + postWord[::-1]) 

#%% 문자열을 여러 문자열로 나누는 split() 메소드 
'사과 배 복숭아 딸기 포도'.split()
'테스크탑 1000000, 노트북 1800000, 스마트폰 1200000'.split()

'테스크탑 1000000, 노트북 1800000, 스마트폰 1200000'.split(',')
'테스크탑 1000000, 노트북 1800000, 스마트폰 1200000'.split(', ')

#%% 정수 형태 두 개의 분리
m, n = '100 200'.split()
m, n

#%% 03-06multinput.py	4개의 수를 입력 받아 합, 평균, 최대, 최소를 출력
m, n, x, y = input('4개의 수 입력 >> ').split()
a, b, c, d = float(m), float(n), float(x), float(y)
print('입력 값: ', a, b, c, d)
sum = a + b + c + d
print('합: ', sum, '평균: ', sum / 4)
print('최대: ', max(a, b, c, d), '최소: ', min(a, b, c, d))

#%%	다양한 문자열 변환 메소드
'python'.upper() #모두 대문자로 변환하여 반환
'PYTHON'.lower() #모두 소문자로 변환하여 반환
'python lecture'.capitalize() #첫 문자만 대문자로 변환하여 반환
'python lecture'.title() #단어마다 첫문자를 대문자로 변환하여 반환
'PyThOn'.swapcase() #소문자와 대문자를 서로 변환하여 반환

#%% center() 메소드
' 파이썬 강좌 '.center(30, '*')
' 파이썬 강좌 '.center(30)
' 파이썬 강좌 '.center(30, '=')

#%% ljust(), rjust() 메소드
'python'.ljust(10)
'python'.ljust(10, '*')
'python'.rjust(10)
'python'.rjust(10, '*')

#%% 공백을 없애는 lstrip() lstrip() strip()
'  python  '.lstrip()
'  python  '.rstrip()
'  python  '.strip()
'  ***python---  '.strip('* -')

#%%
'234'.zfill(5)
'abc'.zfill(5)
'-345'.zfill(8)
'+7897'.zfill(8)

#%%
'python'.startswith('py')
'python'.endswith('on')
'fortran99'.isidentifier()
'99fortran'.isidentifier()

'Python'.islower()
'PYTHON'.isupper()
'Python Lecture'.istitle()
'PythoYTHON Lecture'.istitle()
'\t '.isspace()

'kotlim'.isalpha()
'35'.isdecimal()
'345b'.isdigit()
'34f'.isnumeric()
'ANSI99C'.isalnum()
'\f'.isprintable()

#%% 출력 정형화 함수 format()
'3 + 4 = 7'
str = '{} + {} = {}'.format(3, 4, 3 + 4)
print(str)

#%% 출력 정형화 {인자순번}
a, b = 10, 4
print('{} * {} = {}'.format(a, b, a * b))
print('{0} / {1} = {2}'.format(a, b, a / b))
print('{1} / {0} = {2}'.format(a, b, b / a))

#%% 출력 정형화 {인자순번:폭유형}
a, b = 10, 3
print('{0:d} / {1:d} = {2:f}'.format(a, b, a / b))
print('{0:5d} / {1:5d} = {2:10.3f}'.format(a, b, a / b))

#%% 출력 정형화 {:폭유형}
a, b = 19, 8
print('{:5b} // {:5o} = {:5d}'.format(a, b, a // b))
print('{0:5b} // {:5o} = {:5d}'.format(a, b, a // b))

#%% 출력 정형화 정수의 다양한 출력
print('12345' * 6)
print('{0:5b}{0:5o}{0:5d}{0:5n}{0:5x}{0:5X}'.format(10))

#%% 형식 유형 f, F
print('1234567890' * 2)
print('{0:10f}{0:10.3F}'.format(3.1415))
print('{0:10f}{0:10.3F}'.format(3.5E1000))
print('{0:10f}{0:10.3F}'.format(float('nan')))

#%% 형식 유형 e, E, g, G
print('1234567890abcdef' * 2)
print('{0:16e}{0:16E}'.format(3.141592))
print('{0:16e}{0:16E}'.format(314.1592))
print('{0:16g}{1:16G}'.format(31.41592E2, 31.41592E20))

#%% 형식 유형 c
print('12345' * 3)
print('{0:5c}{1:5c}{2:5c}'.format(0x41, 65, 0o101))
print('{0:<5c}{1:^5c}{2:>5c}'.format(0x42, 67, 0o104))

#%% 형식 유형 %
print('{0:8.1%} {0:.2%} {0:f}'.format(.345))

#%% 형식 유형 s
print('1234567890' * 3)
print('{:10s}{:10s}{:10s}'.format('java', 'python', 'kotlin'))
print('{0:<10s}{0:^10s}{0:>10s}'.format('java'))
print('{0:<10s}{0:^10s}{0:>10s}'.format('python'))

#%% C 스타일 정형화 출력
'%d - %x = %o' % (30, 20, 30 - 20)
print('%d ** %x = %o' % (3, 2, 3 ** 2))
print('%10.2f' % 2.718282)
print('%10c' % 'p')
print('%10s' % 'python')
print('%d%%' % 99)

#%% 중간점검 3, 03-chk03.py 
print('python'.replace('p', 'P'))
print('#'.join('C++'))
print('python'.find('th'))
print('python'.index('py'))
print('정수,실수,문자열,논리'.split(','))

#%% 중간점검 4, 03-chk04.py 
print('p{}{}'.format('y', 'charm'))
print('{0:d} {0:b} {0:o}'.format(7))
print('{2} {1} {0}'.format(5, 20, 20 - 5))
print('{0:6.3f} {0:5.2f}'.format(31.456))
print('%d %f' % (3.14, 3.14))

#%% 3장 3절

#%% 논리 값
print(True, False)
type(True)
bool(0), bool(0.0), bool('')
bool(10), bool(3.14), bool('python')

#%% 논리 값은 정수로 각각 1 0
int(True), int(False)

#%% 논리곱 연산자 & and
True & True, True and True
True & False, True and False
False & True, False and True
False & False, False and False 

#%% 논리합 연산자 | or
True | True, True or True
True | False, True or False
False | True, False or True 
False | False, False or False 

#%% 배타적 논리합 연산자 ^
True ^ True
True ^ False
False ^ True
False ^ False

#%% not 연산자
not True, not False

#%% not and or 우선순위
not False and True
(not False) and True
not True or True and False
(not True) or (True and False)

#%% 관계 연산자
ord('a'), ord('A'), ord('\0'), ord('B')
8 > 2,  'a' > 'A' 
8 >= 2, 'a' >= 'A'
8 < 2,  'a' < 'aB'
8 <= 2, 'a' <= 'aB'
8 == 2, 'a' == 'aB'
8 != 2, 'a' != 'aB'

#%% 03-07relationop.py	문자열과 실수의 관계 연산
print('cat' > 'dog')
print('tiger' < 'lion')
print(3.5 <= 3.56)
speed = 60
print(50 > speed)
print(80 < speed)
print(50 < speed and speed <= 80)
print(50 < speed <= 80)
print(True > False)

#%% 03-08bmiop.py	키와 몸무게로 비만도 지수 BMI 판정
h, w = input('당신의 키(cm)와 몸무게(kg)는? >> ').split() 
#h, w = 169, 66
height = float(h)  
weight = float(w)
bmi = weight / (height/100)**2  

print('키:%6.1f(cm), 몸무게:%5.1f(km), BMI:%5.1f' % (height, weight, bmi))
print('{} {}'.format('고도비만', 40 <= bmi))
print('{} {}'.format('중등도비만', 35 <= bmi < 40))
print('{} {}'.format('비만', 30 <= bmi < 35))
print('{} {}'.format('과체중', 25 <= bmi < 30))
print('{} {}'.format('정상', 18.5 <= bmi < 25))
print('{} {}'.format('저체중', bmi < 18.5))

#%% 논리 값의 산술 연산
40 * True, 30 * False

#%% 03-09epowerbase.py	전기 사용량의 기본 요금 계산
usage = float(input('가정의 전기 사용량(kWh)은 >> '))
#usage = 300
less200 = usage <= 200 
less400 = 200 < usage <= 400 
greater400 = 400 < usage

base = 730 * less200 + 1260 * less400 + 6060 * greater400
print('전기 사용량(kw): %d, 기본요금(원): %d' % (usage, base))

#%% 멤버쉽 연산 in
'p' in 'python', 'h' in 'python'
'pi' in 'python', 'then' in 'python'
'java' not in 'python', 'c' not in 'python'

#%% 03-10keywordin.py	멤버쉽 검사 in으로 배운 파이썬 키워드 검사
inkey = input('배운 파이썬 키워드를 입력하세요 >> ')
#inkey = 'key'
keywords = "'False', 'True', 'and', 'in', 'is', 'not', 'or'" 
print('입력 단어 {}, 키워드인가? {}'.format(inkey, inkey in keywords))

#%% 비트 연산자
m, n = 0, 0
'{} {} {} {} {}'.format(m, n, m & n, m | n, m ^ n)  
m, n = 0, 1
'{} {} {} {} {}'.format(m, n, m & n, m | n, m ^ n)  
m, n = 1, 0
'{} {} {} {} {}'.format(m, n, m & n, m | n, m ^ n)  
m, n = 1, 1
'{} {} {} {} {}'.format(m, n, m & n, m | n, m ^ n)  

#%% 비트 논리 연산 
a, b = 23, 57
print('10진수 {0:2d}, 2진수 {0:08b}'.format(a))
print('10진수 {0:2d}, 2진수 {0:08b}'.format(b))
print('10진수 {0:2d}, 2진수 {0:08b}'.format(a & b))
print('10진수 {0:2d}, 2진수 {0:08b}'.format(a | b))
print('10진수 {0:2d}, 2진수 {0:08b}'.format(a ^ b))

#%% 03-11extractbit.py	비트 연산자 &로 정수의 특정 비트 알아 내기 
a = int(input('정수 하나를 입력하세요 >> '))
#a = 23
mask = 0b1111 #0xf도 가능
print('정수 {0} 2진수로는 {0:b}'.format(a))
print('가장 오른쪽 4비트: {0:04b} 정수로는 {0}'.format(a & mask))

#%%
origin = 0b101011
mask = 5
encription = origin ^ mask
result = encription ^ mask
origin == result
print('{:08b}'.format(origin))
print('{:08b}'.format(mask))
print('{:08b}'.format(encription))

#%% 03-12encryption.py	비트 배타적 논리합 ^으로 ID의 암호화 
orgPwd = int(input('ID로 사용할 여덟자리의 정수를 입력하세요 >> '))
#orgPwd = 12345678
keyMask = 27182818 #키로 사용할 정수 하나를 저장 
encPwd = orgPwd ^ keyMask #ID를 암호화시켜 저장

print('입력한 ID: %d' % orgPwd)
print('암호화하여 저장된 ID: %d' % encPwd)

inPwd = int(input('로그인할 ID를 입력하세요 >> ))
#inPwd = 12345678
result = encPwd ^ keyMask #키로 암호화된 것을 복호화
print('로그인 성공: {}'.format(inPwd == result))


#%% 비트 보수 연산 ~ 
n = 34
print('10진수 {0:3d}, 2진수 {0:08b}'.format(n))
print('10진수 {0:3d}, 2진수 {0:08b}'.format(~n))
print('10진수 {0:3d}, 2진수 {0:08b}'.format(~~n))
print('10진수 {0:3d}, 2진수 {0:08b}'.format(~n + 1))

#%% 음수 정수 표현
mask = 0xff
print('{}의 가장 오른쪽 8비트: {:8b}'.format(-34, -34 & mask))

#%% 실습 예제
minus = -35
print('10진수 {0:3d}, 2진수 {0:08b}'.format(minus))
print('{0:3d}의 32비트 2진수 표현 {1:b}'.format(minus, minus & 2**16-1))

#%% 비트 이동 연산자 >>
a = 0b00010111
print('10진수 {0:3d}, 2진수 {0:08b}'.format(a))
print('10진수 {0:3d}, 2진수 {0:08b}'.format(a >> 1))
print('10진수 {0:3d}, 2진수 {0:08b}'.format(a // 2))
print('10진수 {0:3d}, 2진수 {0:08b}'.format(a >> 2))
print('10진수 {0:3d}, 2진수 {0:08b}'.format(a // 2**2))
 
#%% 비트 이동 연산자 >>
a = 0b00010111
print('10진수 {0:3d}, 2진수 {0:08b}'.format(a))
print('10진수 {0:3d}, 2진수 {0:08b}'.format(a << 1))
print('10진수 {0:3d}, 2진수 {0:08b}'.format(a * 2))
print('10진수 {0:3d}, 2진수 {0:08b}'.format(a << 2))
print('10진수 {0:3d}, 2진수 {0:08b}'.format(a * 2**2))

#%% 03-13bitshiftop.py	표준 입력으로 비트 이동 연산 << 계산 
num = int(input('이동 연산 num << cnt를 수행할 정수 num 입력 ? '))
cnt = int(input('이동 연산 num << cnt를 수행할 정수 cnt 입력 ? '))
#num = 0b00010111
#cnt = 3
print('{0:032b} {0:8d} :num'.format(num))
print('{2:032b} {2:8d} :{0} << {1}'.format(num, cnt, num << cnt))
print('{2:032b} {2:8d} :{0} * 2**{1}'.format(num, cnt, num * 2**cnt))

#%% 연산 우선 순위
print(   20 +  30 // 5   >> 2  | 1 )
print( ((20 + (30 // 5)) >> 2) | 1 )
print(   3 << 2  < 100  and    3 ** 3  >> 2  >= 5  )
print( ((3 << 2) < 100) and (((3 ** 3) >> 2) >= 5) )

#%% 03-14leapyear.py	표준 입력의 연도가 윤년인지 검사하여 출력
year = int(input('윤년을 검사할 연도 입력 >> '))
#year = 2020
print('입력한 연도: %d' % year)
cond1 = year % 4 == 0
cond2 = year % 100 != 0
cond3 = year % 400 == 0
result1 = cond1 and cond2 or cond3
print('개별 검사 {} and {} or {}: {}'.format(cond1, cond2, cond3, result1))
result2 = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print('통합 검사: %s' % result2)

#%% 중간점검 5, 03-chk05.py 
print('python' < 'Python')
print(50 <= 50 < 60)
print(3 < 5 and 10 < 20)
print(3 >= 5 or not (10 < 20))
print('셋' not in '리스트 튜플 딕셔너리 셋')

#%% 중간점검 6, 03-chk06.py 
print(0b100 & 0b011)
print(5 | 2)
print(~5)
print(0b1100 >> 2)
print(10 << 2)

#%% 프로젝트 Lab1 03-pl01-discount.py	난이도: 응용
#할인률에 따른 할인 가격
price = int(input('총 가격(원 가격) 입력 >> '))
#price = 18000

rate1 = (10000 <= price < 20000) * 1/100
rate2 = (20000 <= price < 40000) * 2/100
rate3 = (40000 <= price) * 4/100
rate = rate1 + rate2 + rate3

discount = price * rate
discPrice = price - discount
print("원 가격:", price, '할인된 가격:', discPrice)
print("할인율:", rate, '할인액:', discount)

#%% 프로젝트 Lab2 03-pl02-extractword.py	난이도: 실전
#단어를 추출하여 회문(palindrome)인지 검사 
str = input('콤마로 구분된 단어 3개 입력 >> ')
#str = '기러기,  level, 아버지'
str = str.replace(' ', '')
w1, w2, w3 = str.split(',')

print('단어: {}, 역순: {}, 회문: {}'.format(w1, w1[::-1], (w1 == w1[::-1])))
print('단어: {}, 역순: {}, 회문: {}'.format(w2, w2[::-1], (w2 == w2[::-1])))
print('단어: {}, 역순: {}, 회문: {}'.format(w3, w3[::-1], (w3 == w3[::-1])))

#%% EOF 종료 