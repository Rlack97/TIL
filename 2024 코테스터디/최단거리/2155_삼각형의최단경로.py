# 20240130 삼각형의 최단경로

# 첫 번째는 '다음 줄의 두번 째 수' 와 '자신의 다음 수'와 연결됨
# 마지막은 '다음 줄의 뒤에서 두번째 수'와 '자신의 직전 수'와 연결됨
# 짝수 번째는 윗줄과, 홀수 번째는 다음 줄과 연결됨

import math
A, B = map(int, input().split())

# A가 항상 작은 수일수 있도록 함
if A > B:
    A, B = B, A

# 삼각형 각 행의 끝 수는 n^2이다.
# 각 수가 몇 번째 행에 있는지 찾으려면, 제곱근의 정수부만 남겨보면 된다.
# 행 내부 인덱스도 기록해두자.
# 1일 경우는 별도로 선언해준다.
if A == 1:
    line_A = 1
    idx_A = 0
else:
    A_sqrt = math.sqrt(A)

    if A_sqrt.is_integer():
        line_A = int(A_sqrt)
    else:
        line_A = int(A_sqrt) + 1

    idx_A = A-(line_A-1)**2-1

B_sqrt = math.sqrt(B)
if B_sqrt.is_integer():
    line_B = int(B_sqrt)
else:
    line_B = int(B_sqrt) + 1

# 행 사이의 거리만큼 이동하게 된다.
# 이 때, 삼각형이 정삼각형인지 역삼각형인지가 중요하다.
# 짝수 줄의 정삼각형은 짝수, 역삼각형은 홀수
# 홀수 줄의 정삼각형은 홀수, 역삼각형은 짝수이다.


def triangle_confirm(line, value):
    if line % 2 == 0:
        if value % 2 == 0:
            result = True
        else:
            result = False
    else:
        if value % 2 == 0:
            result = False
        else:
            result = True

    return result


tri_A = triangle_confirm(line_A, A)
tri_B = triangle_confirm(line_B, B)

# A를 맨 위 꼭짓점으로 해서 B가 있는 곳까지 삼각형을 그렸을 때,
# B가 삼각형 내부에 있다면 모양에 따라 이동횟수가 동일하다.

# 두 행 사이의 거리
cnt = abs(line_A-line_B)

# B행의 양 끝값의 거리는 2cnt. 값은???
# 왼쪽 꼭짓점은 B가 있는 행의 idx_A번째 값.
# 오른쪽 꼭짓점은 B가 있는 행의 2cnt + idx_A번째 값.
# B행의 숫자들은 ((line_B-1)**2+1)과 line_B**2사이의 값.
list_B = list(range((line_B-1)**2+1, line_B**2+1))
left = list_B[idx_A]
right = list_B[2*cnt + idx_A]

# A가 정삼각형일때
if tri_A == True:
    if left <= B <= right:
        if tri_B == True:
            answer = 2*cnt
        else:
            answer = 2*cnt-1
    elif B < left:
        answer = 2*cnt + (left-B)
    elif B > right:
        answer = 2*cnt + (B-right)


# A가 역삼각형일 때
if tri_A == False:
    if left <= B <= right:
        if tri_B == True:
            answer = 2*cnt + 1
        else:
            answer = 2*cnt
    elif B < left:
        answer = 2*cnt + (left-B)
    elif B > right:
        answer = 2*cnt + (B-right)

print(answer)
