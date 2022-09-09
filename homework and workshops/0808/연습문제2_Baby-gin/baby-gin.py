# 연습문제2_Baby-Gin 풀이
# 2022-08-08
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
n = 0
for q in range(T):
	n += 1
	num = int(input())
	c = [0]*12        # 인덱스 에러/조건문 사용을 방지하기 위해 9 + 3을 사용

	for i in range(6):
		c[num % 10] += 1 
		num//= 10          # 각 자릿수의 값을 구하고, c에 할당하는 count 정렬

	i = 0
	tri = run = 0
	while i < 10:
		if c[i] >= 3: # 트리플렛 조사 후 삭제하는 코드
			c[i]-= 3
			tri += 1
			continue   
		elif c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 : # 런 조사 후 데이터 삭제
			c[i] -= 1
			c[i+1] -= 1
			c[i+2] -= 1
			run += 1
			continue
		i += 1       #반복 횟수 제한 (9회)

	if run + tri == 2: # 둘 다 참(1) 일 경우 베이비진 확정
		k = 1
	else: 
		k = 0
	
	

	print(f'#{n} {k}')