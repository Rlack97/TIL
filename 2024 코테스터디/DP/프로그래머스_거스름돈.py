def solution(n, money):
    # 금액별 방법의 수 dp 리스트
    cnt = [0] * (n+1)
    cnt[0] = 1
    
    # 각 동전 종류별
    for m in money:
        # 해당 동전의 값보다 큰 값들에 대해서 (2원으론 1원을 못주잖아)
        for j in range(m,n+1):
            
            # 해당 위치에서 사용중인 코인값을 뺀 위치 값을 추가해줌
            cnt[j] += cnt[j-m]
    
    return cnt[n] % 1000000007