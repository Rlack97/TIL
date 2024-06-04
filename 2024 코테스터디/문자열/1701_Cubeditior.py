# KMP 알고리즘의 failure 배열?

# kmp 알고리즘의 핵심은 패턴의 접두사와 접미사 개념을 적극 활용하여 
# '반복되는 연산을 얼만큼 건너뛸 수 있는 지'에 대해 집중한다는 것이다.
# 패턴 내에 존재하는 접두사와 접미사가 '일치' 한다면 접미사를 접두사로 다시 바라봄으로써 
# 문자열 탐색을 이어서 진행할 수 있기 때문이다.
import sys
input = sys.stdin.readline

def make_table(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return max(table)


str = input()
ans = 0
for i in range(len(str)):
    ans = max(ans, make_table(str[i:len(str)]))
    # 가능한 모든 하위문자열 = 문자열 왼쪽에서 한 글자씩 줄인다



print(ans)
