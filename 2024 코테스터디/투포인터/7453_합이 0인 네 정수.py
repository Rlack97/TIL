import bisect
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())  # 배열의 크기
    A, B, C, D = [], [], [], []

    for _ in range(N):
        a, b, c, d = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
        D.append(d)

    # 두 배열씩 묶어서 합을 구해준다.
    ab, cd = [], []

    for i in range(N):
        for j in range(N):
            ab.append(A[i] + B[j])
            cd.append(C[i] + D[j])

    # 두 배열 모두 오름차순으로 정렬
    ab.sort()
    cd.sort()

    # left는 ab 배열의 시작 부분, right는 cd 배열의 마지막 부분
    left, right = 0, len(cd)-1
    res = 0

    while left < len(ab) and right >= 0:
        tmp = ab[left] + cd[right]

        if tmp > 0:  # 합이 0보다 클 경우 right에 -1을 해주어 합을 줄여준다.
            right -= 1
        elif tmp < 0:  # 합이 0보다 작을 경우 left에 +1을 해주어 합을 높여준다.
            left += 1
        else:  # 0일 경우에는 각각의 값이 배열에 몇 개 존재하는지를 체크해야 한다.
            # upperBound와 lowerBound를 사용하여 배열에 같은 값이 몇 개 있는지를 구할 수 있다.
            abLeft, abRight = bisect.bisect_left(
                ab, ab[left]), bisect.bisect_right(ab, ab[left])
            cdLeft, cdRight = bisect.bisect_left(
                cd, cd[right]), bisect.bisect_right(cd, cd[right])

            # upperBound - lowerBound를 통해서 같은 값이 몇 개 있는지를 구하고
            # 두 값을 곱하여 경우의 수를 카운트한다.
            # 그 후, left는 upperBound로 right는 lowerBound-1로 설정하면
            # 다시 새로운 값부터 합이 0이 되는 경우를 체크할 수 있다.
            res += (abRight - abLeft) * (cdRight - cdLeft)
            left = abRight
            right = cdLeft - 1

    print(res)
