import sys
input = sys.stdin.readline

S = list(input().strip()) # 삼백만

# ㅋㅋ루ㅋㅋ문자열의 조건
# 1. R로만 이루어져 있음
# 2. ㅋㅋ루ㅋㅋ문자열 양끝에 K가 하나씩 붙어있음
# 문자열의 부분 수열 중 가장 긴 ㅋㅋ루ㅋㅋ문자열의 길이
# 부분 수열 = 중간 문자를 지워도 됨.

# 기본이 되는 R로만 이루어진 문자열의 최대길이 + 해당 문자열 기준 앞뒤로 짝이 맞는 K의 갯수

# num_R = S.count('R')

# left, right = 0,0

# left = S.find('R') -1

# if left == -2 and S[0] != 'R':
#   print(-1)
# else:
#   r_S = ''.join(reversed(S))
#   right = len(S) - r_S.find('R')

#   K_pair = min(S[:left+1].count('K'), S[right:].count('K'))
#   print(num_R + K_pair*2)
# 반례 : RKKKKKKRKKKKKKR등 R만 고르는 액션을 취하는 것 자체가 짧은 값을 반환할 

# 거꾸로 K의 갯수를 샌다
# 양 끝에서 R을 만날때까지의 K값을 기록
# 두 값 중 작은 값 * 2+1 + R갯수가 ㅋㅋ루ㅋㅋ문자열의 길이가 된다
# 이후 K갯수가 작은 쪽의 탐색을 진행한다

l_cnt = []
r_cnt = []

# 각 방향에서 R을 만나는 지점마다 그 이전까지의 K 갯수를 기록
cnt = 0
for s in S:
  if s == 'K':
    cnt += 1
  else:
    l_cnt.append(cnt)

cnt = 0
for s in S[::-1]:
  if s == 'K':
    cnt += 1
  else:
    r_cnt.append(cnt)

r_cnt.reverse()

l, r = 0, len(r_cnt)-1
ans = 0
while l<=r:
  # min은 현 포인터 기준 양끝 K의 짝의 수
  # r - l + 1 구간 내 R의 갯수를 의미 (????)
  ans = max(ans, r - l + 1 + min(l_cnt[l], r_cnt[r])*2)

  if l_cnt[l] < r_cnt[r]:
    l+=1
  elif l_cnt[l] > r_cnt[r]:
    r-=1
  else:
    l+=1
    r-=1

print(ans)
