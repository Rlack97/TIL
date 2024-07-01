# 그리디 
import sys
input = sys.stdin.readline

S = str(input())
#a와 그 뒷부분에 있는 b를 지운다 (바로 뒤일 필요 없음)
#bc를 지운다 (마찬가지)
#시행할 수 있는 최대횟수

#A + B
#B + C
# 핵심관찰
# 1. AB, BC 조합은 B가 중복된다. B가 충분히 많아야 최대 시행이 가능해짐
# 2. B를 AB 만드는데 써버리면 만들 수 있는 BC 수가 줄어듬
# 3. 가능한 AB, BC 갯수보다 더 많은 값은? B가 해당 갯수보다 많을 때.
# 답 = min(AB+BC의 수, B의 수)

# A의 갯수를 누적시키면서 B가 나오면 카운트 +1, A갯수 -1 형태로 기록


AB = 0
BC = 0
A = 0
B = 0
B_cnt = 0


for s in S:
  if s == 'A':
    A += 1
  elif s == 'B':
    B += 1
    B_cnt += 1
    if A:
      A -= 1
      AB += 1
  elif s == 'C':
    if B:
      B -= 1
      BC += 1

print(min(AB+BC, B_cnt))