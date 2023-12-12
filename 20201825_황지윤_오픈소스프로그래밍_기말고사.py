#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201825 이름 : 황지윤

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target): # 함수 정의
    # 추가된 부분
    if target in my_string: # 만약 target 이 my_string 안에 포함된다면 
        return 1 # 1을 반환
    else: # 그렇지 않다면
        return 0 # 0을 반환
 
# 테스트
test_my_string = "opensource" # 테스트용 문자열
test_target = "pen" # 테스트용 부분 문자열

result = solution(test_my_string, test_target) # solution함수 사용하여 결과 result에 저장
print(result) # 결과를 출력


# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = 여러분의 좌우명 또는 인상 깊었던 말을 쓰시오.

def solution(letter):
    # morse부호 코드와 그에 해당하는 알파벳을 매핑한 딕셔너리
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    answer = ''

    # 추가된 부분
    letter_pieces = letter.split() # 공백을 기준으로 문자열 나눔, 분리된 문자열은 리스트로 반환됨
    
    # for문 사용하여 morse부호 코드를 알파벳으로 바꾸고 그 결과를 answer에 저장함
    for piece in letter_pieces: # piece 변수에 현재의 morse부호코드 조각이 들어가서 반복문 수행
        answer += morse[piece] # 해당 morse부호 코드에 대응하는 알파벳을 answer에 추가하는 역할 수행
    return answer

# 테스트
# 테스트용 morse부호 코드 문자열 
morse_test= ".-.. .. -.- . .- .-.. .-- .- -.-- ... - .... . ..-. .. .-. ... - - .. -- ."
# 위의 solution함수 사용하여 morse 부호 코드를 알파벳으로 변환
result = solution(morse_test)
# 변환된 결과 출력
print(result)


# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
    # 추가된 부분
    
    age = str(age) # age를 문자열로 바꿔서 각각의 숫자를 알파벳으로 매핑시킴
    age = age.replace("0","a") # 0에 해당하는 숫자 알파벳 a로 매핑
    age = age.replace("1","b") # 1에 해당하는 숫자 알파벳 b로 매핑
    age = age.replace("2","c") # 2에 해당하는 숫자 알파벳 c로 매핑
    age = age.replace("3","d") # 3에 해당하는 숫자 알파벳 d로 매핑
    age = age.replace("4","e") # 4에 해당하는 숫자 알파벳 e로 매핑
    age = age.replace("5","f") # 5에 해당하는 숫자 알파벳 f로 매핑
    age = age.replace("6","g") # 6에 해당하는 숫자 알파벳 g로 매핑
    age = age.replace("7","h") # 7에 해당하는 숫자 알파벳 h로 매핑
    age = age.replace("8","i") # 8에 해당하는 숫자 알파벳 i로 매핑
    age = age.replace("9","j") # 9에 해당하는 숫자 알파벳 j로 매핑
    return age # 변환된 나이 리턴

# 테스트
test_age = 100 # 테스트용 나이 입력
result = solution(test_age)  # solution 함수 호출하여 나이를 알파벳으로 변환
print(result) # 변환된 결과(알파벳) 출력


# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000


# 아래와 같이 가정하고 문제를 품
# r1 = 작은 원의 반지름
# r2 = 큰 원의 반지름
# x = 현재 x좌표
# answer = 정수 좌표의 총 개수 누적값
# result = 최종적인 점의 개수

def solution(r1, r2):
    answer = 0 # 초기값 0으로 설정

# 추가한 부분

    # r2까지 x를 증가시키면서 각 x에 대한 점의 개수를 계산
    for x in range(1, r2 + 1):
        # 각 x에 대한 점의 개수를 solution1 함수를 통해 계산하고 그 값을 answer에 더함
        answer += solution1(x, r1, r2)

    # 최종적인 점의 개수 
    # 각 x에 대한 점의 개수를 2배로 곱한 후,
    # r1과 r2사이의 원 중심에서 가장 바깥쪽에 있는 두 원에 해당하는 둘레의 길이를 더하여 결과 얻기
    result = 2 * answer + 2 * (r2 - r1 + 1) 
    return result
    
    
def solution1(x, r1, r2):
    R1 = r1 ** 2 # 작은 원의 반지름 제곱한 값 R1에 저장
    R2 = r2 ** 2 # 큰 원의 반지름 제곱한 값 R2에 저장
    X = x ** 2 # 현재 x의 제곱값 X에 저장

    y_upper = (R2 - X) ** 0.5 # 현재 x에 대한 큰 원의 위의 경계에 있는 y 값

    # x가 r1보다 작을 때
    if X < R1:

        y_lower = (R1 - X) ** 0.5 # 현재 x에 대한 작은 원의 아래 경계에 있는 y값 
        # y_upper와 y_lower 사이의 정수인 y의 개수 계산
        return 2 * int(y_upper) - 2 * int(y_lower) + is_integer(y_lower)
    # x가 r2와 같을 때
    elif X == R2:
        return 1
    # x가 r1과 r2 사이에 있을 때
    else:
        # y_upper의 정수 부분까지의 개수 계산
        return 2 * int(y_upper) + 1

# 주어진 값이 정수인지를 확인하는 함수
def is_integer(value):
    return value.is_integer() 

# 테스트할 반지름 값 설정
r1 = 4
r2 = 6

# 솔루션 함수 호출
result = solution(r1, r2)

# 결과 출력
print(result)


# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
    # 추가된 부분
    length = list() # 각 숫자의 길이를 저장하는 빈 리스트 만들기
    temp = list() # 각 숫자를 문자열로 변환하여 저장하는 빈 리스트 만들기

    for number in numbers:
        temp.append(str(number)) # 각 숫자를 문자열로 변환하여 temp 리스트에 추가

    for number in temp:
        length.append(len(number)) # 각 숫자의 길이를 length 리스트에 추가
    
    temp = [] # 빈 리스트 만들기

    for number in numbers:
        temp.append(str(number)) # 주어진 숫자들을 문자열로 변환하여 temp 리스트에 추가

    # solution1 함수는 주어진 문자열 x를 3번 반복한 값을 반환하는 함수
    def solution1(x):
        return x * 3
    
    # temp 리스트를 solution1 함수를 key로 사용하여 내림차순으로 정렬
    # 문자열을 길이에 따라 정렬하기 위해서 3번 반복한 값을 기준으로 정렬했음
    temp.sort(key=solution1, reverse=True)

    # 정렬된 문자열을 이어붙여서 가장 큰 수 생성
    answer = ''.join(temp)

    # 결과를 정수로 변환하여 문자열로 다시 변환
    result = str(int(answer))

    return result

# 테스트
test_numbers = [8, 30, 17, 2, 23] # 테스트할 정수
result = solution(test_numbers) # solution 함수에 테스트할 정수 넣어서 결과 result에 저장
print(result) # 결과 출력