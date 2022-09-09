# 4880_토너먼트 카드게임 풀이
# 2022-08-23

import sys
sys.stdin = open('input.txt', 'r')

# 가위바위보 함수
def rcp(a, b):
    if num[a] == num[b] or num[a] - num[b] == -2 or num[a] == num[b] +1:
        # 비기거나
        # 1 : 3 이거나
        # 이긴 경우 a 반환
        return a

    else:
        return b
    # 나머지는 b 반환

# 나누기 함수 (시작, 끝 지점)
def winner(s, e):
    if s == e:
        return s
    # 시작과 끝이 같으면 == 혼자 남으면
    # 자기 자신을 반환

    m = (s+e)//2
    # 중간지점 설정

    g1 = winner(s, m)
    g2 = winner(m+1, e)
    # 앞 뒤 구간 나누기

    return rcp(g1, g2)
    # 앞뒤구간에서 승자의 인덱스를 반환


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    print('#{} {}'.format(tc, winner(0, N-1)+1))
    # 인덱스값 +1


