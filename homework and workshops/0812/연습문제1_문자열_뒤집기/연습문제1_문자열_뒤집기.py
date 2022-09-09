# 연습문제1_문자열뒤집기 풀이
# 2022-08-12

from ntpath import join
import sys
sys.stdin = open('input.txt','r')


s = input()

# slicing 활용

s = s[::-1]
print(s)

# revese 메소드 사용

s = input()

s= list(s)
s.reverse()
s=''.join(s)
    
print(s)


# for문 

s = input()

reversed_s = ''

for i in range(len(s)-1,-1,-1):
    reversed_s+=s[i]
print(reversed_s)

# 앞뒤를 교환

s= 'algorithm'
list_s = list(s)
for j in range(len(s)//2):
    list_s[j], list_s[-(j+1)] = list_s[-(j+1)], list_s[j]
list_s = ''.join(list_s)
print(list_s)
