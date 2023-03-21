# 2775_부녀회장 풀이
# 2023/03/21

import sys
sys.stdin = open('input.txt','r')

def apart(a,b) :
  apartment = [[i for i in range(1,b+1)]] 
  # 리스트 컴프리헨션으로 2중리스트 초기 세팅 (0층)
  for height in range(1,a+1):
    # 0층이 있으므로 1층부터 a층까지
    list = []
    for i in range(b):
      # 1호실부터 b호실까지
      people = sum(apartment[height-1][:i+1])
      # 현재 높이 heigth보다 1층 낮은 곳에서, 현재 호실 까지의 사람의 합
      # 0 = 1호실 이므로 i +1
      list.append(people)
      # 구한 리스트를 이중리스트에 추가
      # 이중리스트의 첫 index값이 층수 -1 값이 됨
    apartment.append(list)
  
  return apartment
      
T = int(input())
maxHeight = 0
maxRoom = 0
need_print = []
for i in range(T):
  k = int(input())
  n = int(input())
  need_print.append([k,n])
  if maxHeight < k:
    maxHeight = k
  if maxRoom < n:
    maxRoom = n
# 답을 구하기 위해 아파트를 dp로 구현
# 문제에서 구할 값을 구하는게 아니라, 제공되는 최댓값으로 만들면 됨.

apartment = apart(maxHeight, maxRoom)

for item in need_print:
  print(apartment[item[0]][item[1]-1])