# 누적합 + 이분탐색

from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

T = int(input())
n = int(input())
list_A = list(map(int,input().split()))
m = int(input())
list_B = list(map(int,input().split()))

# 배열 누적합 및 부 배열 구하기
sumed_list_A = [0] * (n+1)
sumed_list_B = [0] * (m+1)

for i in range(n):
  sumed_list_A[i+1] = sumed_list_A[i] + list_A[i]

for i in range(m):
  sumed_list_B[i+1] = sumed_list_B[i] + list_B[i]

sub_array_A = []
sub_array_B = []

for i in range(n+1):
  for j in range(i+1,n+1):
    sub_array_A.append(sumed_list_A[j] - sumed_list_A[i])
    

for i in range(m+1):
  for j in range(i+1,m+1):
    sub_array_B.append(sumed_list_B[j] - sumed_list_B[i])

sub_array_A.sort()
sub_array_B.sort()

count = 0

for i in range(len(sub_array_A)):
      # 더해서 T가 되는 배열 B의 부 배열의 경우의 수 구하기
      #오름차순 정렬된 배열에서 bisect right(a)- bisect left (a) = 배열에서의 a의 개수
  r = bisect_right(sub_array_B, T - sub_array_A[i])
  l = bisect_left(sub_array_B, T - sub_array_A[i])
  count += r-l

print(count)
