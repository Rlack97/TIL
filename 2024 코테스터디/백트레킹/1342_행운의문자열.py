import sys
from collections import defaultdict
input = sys.stdin.readline

words = defaultdict(int)
S = str(input().rstrip())

# 단어 사전에 기록
for s in S:
  words[s] += 1

# 행운의 문자열 = 각 문자열의 앞 뒤가 모두 다른 문자열이어야 함
# ex) abababa 등
cnt = 0



# 이전 글자, 문자열 수를 인수로 받는 BFS
def BFS(pre, length):
  global cnt

  # 행운의 문자열 조건에 맞는 재배치가 끝났다면
  if length == len(S):
    cnt += 1

  for k in words.keys():
    # 바로 앞의 글자와 같거나 다 쓴 글자이면 패스
    if k == pre or words[k] == 0:
      continue
    else:
      words[k] -= 1
      BFS(k,length+1)
      words[k] += 1

BFS('',0)
print(cnt)

  