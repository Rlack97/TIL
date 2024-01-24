#17609 회문
# 시간복잡도 O(N)?

N = int(input())
for n in range(N):
  answer = 0
  words = list(map(str,input()))
  #양 끝을 가리키는 포인터 설정
  left_idx = 0
  right_idx = len(words)-1

  while (left_idx < right_idx):
  # 앞뒤가 동일하면 포인터를 이동시킴
    if (words[left_idx] == words[right_idx]):
      left_idx += 1
      right_idx -= 1
    
    # 동일하지 않은 경우
    else : 
      # 유사회문 검사
      # 각 포인터를 한 번씩 더 이동시켰을 때 회문이 충족되는지 확인
      # 왼쪽 포인터를 오른쪽으로 이동했을 때, 내부가 회문인가?
      if (words[left_idx+1:right_idx+1] == words[left_idx+1:right_idx+1][::-1]):
        answer = 1
        break
      elif (words[left_idx:right_idx] == words[left_idx:right_idx][::-1]):
        answer = 1
        break
      # 아닐 경우 회문 아님
      else:
        answer = 2
        break
  print(answer)
      

