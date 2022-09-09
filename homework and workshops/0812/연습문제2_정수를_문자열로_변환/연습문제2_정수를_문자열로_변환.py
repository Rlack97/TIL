# 연습문제2_정수를 문자열로 변환 풀이
# 2022-08-12

from math import remainder


def itoa(i):
    if i == 0:
        return '0'
    
    if i < 0:
        flag = False
        i = -(i)
    else:
        flag = True

    result = ''
    while i:
        i,remainder = i // 10, i % 10
        result = chr(ord('0') + remainder) + result

    if flag == True:
        return result
    else:
        return '-' + result

print(itoa(-3))
print(itoa(4))
print(itoa(5))
print(itoa(0))

    