def min_length_subarray_sum(N, S, sequence):
    start = 0
    end = 0
    current_sum = 0
    min_length = float('inf')
    
    while end < N:
        # 현재 부분합에 끝 포인터가 가리키는 값을 더한다
        current_sum += sequence[end]
        end += 1
        
        # 현재 부분합이 S 이상일 때, 시작 포인터를 이동시키며 최소 길이를 찾는다
        while current_sum >= S:
            min_length = min(min_length, end - start)
            current_sum -= sequence[start]
            start += 1
            
    # 만일 최소 길이가 갱신되지 않았다면 조건을 만족하는 부분합이 없음을 의미
    if min_length == float('inf'):
        return 0
    else:
        return min_length

# 입력 받기
N, S = map(int, input().split())
sequence = list(map(int, input().split()))

# 결과 출력
result = min_length_subarray_sum(N, S, sequence)
print(result)