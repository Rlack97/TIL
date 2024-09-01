import sys
input = sys.stdin.readline

a,b = map(int,input().split())
answer = b-a+1

multi = [False] * (b-a+1)

# 최댓값의 제곱근 +1로 범위를 잡는다
for i in range(2, int(b**0.5+1)):
    #제곱값
    square = i ** 2
    # 최솟값 / 제곱값 +1(= 제곱근 범위)부터, 배율만큼 건너 뛰며 영역 순회
    for j in range((((a-1)//square)+1)*square, b+1, square):
        
        # 배수처리 및 갯수 제외
        if not multi[j-a] :
            multi[j-a] = True
            answer -= 1 

print(answer)

# 채 사용이 두 번이 되니 시간초과가 발생한다.
# 바로 제곱근 사용을 통해 소수에 접근해야 할 듯