# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:32:33 2019

2장 본문의 모든 코드: ch02All-code.py
@author: Kang Hwan Soo
"""
#%% 2장 1절
 
#%% 간편 문자열 이해 
'P'
"python"
'27'
"3.14"

#%% 문자열 이해와 출력
print("Hello World!")
print('Hello Python!')

print("Hello string!') #구문 오류

#%% 문자열 연산자 + * 
print("문자열" '연결')
print("python " + "program")

print('방가 ' * 3)
print(4 * '콜록 ')

print('파이썬' * '언어') #오류

#%% 02-01stringop.py 문자열 연결과 반복 연산자 + *의 활용 
print("원의 원주율 " + '3.141592')
print("python " 'programming ' + 'language')
print('파이썬 언어는' + " 강력하다")
print('파이썬 ' + "언어! " + 3 * "방가 ")

#%% 여러 줄 문자열: 삼중 따옴표
print('''String operator + and * are
very easy!''')
print("""비록 그대가 우둔하여 그 방법이 처음에는 명확해 보이지 않을지라도
지금 하는게 아예 안하는 것보다 낫다.""")

#%% 주석 #
#print()는 콘솔에 자료를 출력하는 함수
print('# 이후는 주석') #한 줄에서 문장 이후에도 주석 사용이 가능

#%% 02-02comments.py	주석 #과 여러 줄 문자열 삼중 따옴표 활용
''' 1-2comments.py 
    2019 3. by Kang Hwan Soo '''
    
print('# 이후는 주석') #한 줄에서 문장 이후에도 주석 사용이 가능 
print('string: "python"') #큰 따옴표 내부에서 작은 따옴표는 문자열
print("number: 1 5 3.14") #문자열 내부에서 숫자도 문자열
print("string: 'python'") #작은 따옴표 내부에서 작은 따옴표는 문자열

#%% 수의 이해 
print(15)
print(3.14)

#%% 수의 이해 
0
000
03
03.14

#%% 수의 계산 
5 + 3
5 - 3
5 * 3
5 / 3

#%% 0으로 나누는 오류
4 / 2
4 / 0

#%% 실수 표현
2.7834e4
2.7834e-4
2.7834E5

#%% 복소수
3 + 5j
3 + 5j + 5 - 2j
(3 + 5j).imag
(3 + 5j).real
(3 + 5j).conjugate()

#%% 일반 나누기와 정수 나누기 
8 / 5
8 // 5
2.8 / 1.2
2.8 // 1.2

-1.5 / 0.2
-1.5 // 0.2

#%% 수의 이해 
5 // 3
5 % 3
divmod(5, 3)
5 ** 3
pow(5, 3)

#%% 산술 연산자 우선순위 
2 ** 2 ** 3
2 ** (2 ** 3)
(2 ** 2) ** 3

#%%
-2 * -5
-2 ** 2
(-2) ** 2

#%% 02-03twopdist.py	두 점 사이의 거리 계산
print(4 ** (1/2))
print( ((3**2 + 4**2)) ** (1/2) ) 
print( ((2-3.1)**2 + (5-4.8)**2) ** (1/2) )

#%% _를 사용, 이동 거리 계산 
60
_
3 * _
_

#%% _ 사용
3 + 4
_
'파'
_
'파이 ' + '썬'*3
_
#print('뱀'*3)
#_

#%%
print(3 * '파')
3 * '파'
_
print((3 * 4))
_

#%% 지구와 달의 거리 km로 표현 
384403900 // 1000
384403900 % 1000

#%% 02-04pay.py	식당에서 식비 지불과 잔돈 받기
print('계산금액')
print(78000)
print('오만원권')
print(78000 // 50000)
78000 % 50000
print('만원권')
print( _ // 10000)
_ % 10000
print('오천원권')
print( _ // 5000 + 1)
print('잔돈')
print(5000 - _ % 5000)
print(5000 - (78000 % 50000) % 10000 % 5000)

#%% 지불과잔돈 교환 쉬운 테스트 프로그램
p = 56000
print('계산금액')
print(p)
print('오만원권')
print(p // 50000)
p % 50000
print('만원권')
print( _ // 10000)
_ % 10000
#(p % 50000) % 10000
print('오천원권')
print( _ // 5000 + 1)
print('잔돈')
print(5000 - (p % 50000) % 10000 % 5000)


#%% 02-05interestrate.py	예금의 단리와 복리 계산	난이도: 기본 
1000000 + (1000000 * 2.3/100) #1년차 총액
1000000 + (1000000 * 2.3/100) + (1000000 * 2.3/100) #2년차 총액
1000000 * (1 + 2.3/100 * 3) #3년차 총액
1000000 * (1 + 2.3/100 * 4) #4년차 총액
1000000 * (1 + 2.3/100 * 5) #5년차 총액
1000000 * (1 + 2.3/100) ** 5 #복리 5년차 총액

#%% 02-06print.py	한 번에 여러 자료 출력	
print(1, 2, -5, 3.14, 2.71828)
print('Hi,', 'Python!')

print('23000원은', '5000원 ?개', '1000원 ?개')
print('5000원', 23000 // 5000, '개')
print('1000원', (23000 % 5000) // 1000, '개')

#%% 함수 eval()
eval('3 + 15 / 2')
eval('4 * 3 % 5')
eval('3 * -2 ** 3')
eval('"java " * 3')

#%% 중간점검 1, 02-chk01.py 
print(10 * 3 / 2)
print(3 - 2 * 3 // 5)
print(81 / -3 ** 2)
print(10 + 3 - 23 % 4)
print(20 // 2 ** 3)

#%% 중간점검 2, 02-chk02.py 
print('*' * 1)
print('*' * 2)
print('*' * 3)
print('*' * 4)
print('*' * 5)

#%% 2장 2절 

#%% type() 함수
type(3)
type(3.14)
pi = 3.14
type(pi)
type('python')
type(3 + 4j)

#%% 변수와 대입 연산자 이해 
unit = 3
3 = unit

#%% 변수와 대입 연산자 이해 
a = b = c = 5
print(a)
print(b)
print(c)
b = 3
print(b)

#%% 변수와 대입 연산자 이해 
5 = 3 + 2
5 == 3 + 2

#%% 키워드 확인 
import keyword
print(keyword.kwlist)

#%% 02-07variable.py	변수 이름 규칙 
value = 10
Value = 200
value
Value
total_price = 100000
coffeePrice = 4500
_month = 11
2020year = 2020 #오류: 수로 시작
sale@ = 20 #오류: 문자 @ 사용 불가
sale price = 16000 #오류: 공백 문자 사용 불가
import = 30 #오류: 키워드 사용 불가

#%% 변수 값 증가 시키기 
value = 1
value = value + 1 #value 값을 1 증가 
print(value)
value + 1 = value #오류 

#%% 복합 대입 연산자 
data = 7
#data 값을 1 증가 
data += 1 #data = data + 1 같은 문장
print(data)
#data 값을 5 증가 
data += 5 #data = data + 5 같은 문장
print(data)

var = 5 
var *= 10 // 3 % 5 # var = var * (10 // 3 % 5)와 같은 문장
print(var)

#%% 복합 대입 연산자 주의
undefined += 2

#%% 다양한 증강 대입 연산자 
var = 5
var += 2
print(var)
var -= 3
print(var)
var *= 5
print(var)
var //= 3
print(var)
var **= 2
print(var)
var %= 7
print(var)
var /= 5
print(var)

#%% 02-08celsius.py	섭씨 온도를 화씨로 변환 
celsius = 37
fahrenhite = celsius * 9/5 + 32 #화씨로 변환 
print('섭씨: ', celsius, ',', '화씨: ', fahrenhite)
celsius += 3 #5도 증가
fahrenhite = celsius * 9/5 + 32 #화씨로 변환 
print('섭씨: ', celsius, ',', '화씨: ', fahrenhite)

#%% 세일 계산 
print(56000 * (100 - 20) / 100)

#%% 02-09sale.py	세일을 적용하여 가격 계산 및 출력
price = 56000
sale = 20
salePrice = price * (100 - sale) / 100
print(salePrice)

#%% 여러 자료의 대입
a, b = 3, 4
print(a, b)

#%% 두 수의 교환
a, b = 5, 9
temp = a
a = b
b = temp
print(a, b)

a, b = 5, 9
b, a = a, b
print(a, b)

#%% 함수 divmod() 이용
28 // 3, 28 % 3
divmod(28, 3)  

a, b = 17, 5 
d, m = divmod(a, b)
print(d, m)  

#%% 02-10moondist.py	만 단위로 지구와 달까지의 거리 출력 
distance = 384400
unit = 10000
manUnit, remainder = divmod(distance, unit) 
print('지구에서 달까지의 거리:', manUnit, '만', remainder, '킬로미터')

#%% 중간점검 3, 02-chk03.py 
30day = 1
in = 1
subtraction = 10
$dallar = 1

#%% 중간점검 4, 02-chk04.py 
a, b = 10, 5
b / a / 2
b ** (a - 8)
a // 3 - b / a
b * (a % 7)

#%% 중간점검 5, 02-chk05.py 
days = 257
months = days // 30
days %= 30
print(months, '달', days, '일')

#%% 2장 3절 

#%% 입력함수 input()
input()
pl = input()
print(pl)

#%% 02-11input.py	학교와 이름을 입력 받아 출력
univ = input('대학은? ')
name = input('이름은? ')
print('대학:', univ, '이름:', name)

#%% 문자열 변환 함수 str() 
str(256) #정수 256을 문자열 '235'로 변환
str(2.71828) #자연수 e 문자열 '2.71828'로 변환

#%% 정수와 실수 변환 함수 int(), float() 
int('6400') #지구의 반지름 6,400km
float('3.141592') #원주율 3.141592

#%% 함수 int(), float()
int(2.71828)
float(3)

#%% 02-12convert.py	함수 int()와 float()에서의 변환 주의
int('python') #일반 글자
int('6400i') #정수에 문자 i가 포함
float('3.141592f') #실수에 문자 f가 포함
int('2.71828') #정수가 아닌 실수 형태
int('0b11') #10진수만 형태만 가능
int(float('2.71828')) #정상적으로 2 반환

#%% 
rate = input('예금 만기 이율(%)은? ')
rate / 100 #rate가 문자열이므로 오류 발생 
float(rate) / 100 # 

#%% 02-13age.py	나이를 입력 받아 만 나이를 출력
age = input('나이는? ')
print('실제 나이는', int(age) + 1) 

#%% 02-14length.py	행성 지구 반지름을 입력 받아 지구 둘레 길이 구하기
planet = input('원하는 행성은? ')
strRadius = input(planet + '반지름은? ')
radius = int(strRadius)
length = 3.14 * radius ** 2
print(planet, '반지름: ', radius)
print(planet, '둘레길이: ', length)

#%% 여러 진법 상수 표현
10
0x1f, 0X1E, 0Xa #16진법 표현  
0o17, 0O16, 0O12 #8진법 표현
0b11, 0B10, 0B1010 #2진법 표현

#%% 
bin(7), bin(16), bin(12)
oct(8), oct(10), oct(12) 
hex(14), hex(15), hex(16)

#%% 02-15base.py	10진수 정수를 입력 받아 2진수, 8진수, 10진수, 16진수 출력
data = int(input('정수 입력 >> '))

print('2진수:', bin(data))    #2진수로 출력  
print('8진수:', oct(data))    #8진수로 출력
print('10진수:', data)        #10진수로 출력
print('16진수:', hex(data))   #16진수로 출력

#%% 진수 문자열을 십진수로 변환 함수 int()
int('17'), int('25', 10) #모두 십진수로 변환
int('11', 2) #2진수 문자열을 십진수로 변환
int('10', 8) #8진수 문자열을 십진수로 변환
int('1A', 16) #16진수 문자열을 십진수로 변환

int('0b11', 0) #2진수로 인식
int('0o11', 0) #8진수로 인식
int('0x11', 0) #16진수로 인식

#%% 02-16hexsys.py	16진수 정수를 입력 받아 2진수, 8진수, 10진수, 16진수 출력
invar = input('16진수 정수 입력 >> ')
data = int(invar, 16) #입력 문자열을 16진수로 인지하여 변환
#여러 진수로 출력
print('2진수:', bin(data))
print('8진수:', oct(data))
print('10진수:', data)
print('16진수:', hex(data))

#%% 중간점검 6, 02-chk06.py 
int('156')
int('0b101', 2)
int('0o11', 8)
int('0xf', 16)

#%% 중간점검 7, 02-chk07.py
name = input("당신의 이름은? ")
print("만나서 반가워요, " + name + "씨!")

#%% 프로젝트 Lab 02-pl01-arithmetic.py	표준 입력한 실수와 연산식의 산술 연산과 결과 출력
num1 = float(input('첫 번째 수 입력 >> '))
num2 = float(input('두 번째 수 입력 >> '))
print('합:', num1 + num2)
print('차:', num1 - num2)
print('곱하기:', num1 * num2)
print('나누기:', num1 / num2)

expression = input('연산식 입력(예 3.2 + 4 * 1.5) >> ')
print('연산식:', expression, '결과:', eval(expression))

#%% 프로젝트 Lab 02-pl02-numconvert.py	여러 진수의 표준 입력한 수를 여러 진수로 출력
base = int(input('입력할 정수의 진수(base)는? '))
invar = input(str(base) + '진수 정수 입력 >> ')
data = int(invar, base) #입력 문자열을 base 진수로 변환
#여러 진수로 출력
print('2진수:', bin(data))
print('8진수:', oct(data))
print('10진수:', data)
print('16진수:', hex(data))

#%% EOF 종료 