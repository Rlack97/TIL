# 순위 240127
# 플로이드 와샬 알고리즘
def solution(n, results):
    # 선수별 승/패를 기록하기 위한 빈 리스트
    players = [[None for _ in range(n)] for _ in range(n)]

    # 각 승패를 기록
    for win, lose in results:
        players[win-1][lose-1] = True
        players[lose-1][win-1] = False

    # 플로이드 와샬 알고리즘을 통한 누락 기록 보충

    for i in range(n):  # 중간 B
        for j in range(n):  # 시작 A
            for k in range(n):  # 끝 C
                if players[j][i] == None:  # 기록이 없을경우 넘어감
                    continue

                # 시작-> 중간점, 중간->끝점이 같을 경우
                # 시작 -> 끝점은 시작 -> 중간점의 값과 같다.
                # 즉, A가 B에게 승리하고 B가 C에게 승리한 경우 A는 C에게도 승리한 것.
                # 패배의 경우도 동일하게 처리.
                if players[j][i] == players[i][k]:
                    players[j][k] = players[j][i]

                    # 그리고 C가 A에게 패배했으므로 해당 값도 채워준다.
                    players[k][j] = not players[j][i]

    answer = 0

    # 완성된 표를 순회하면서 갯수를 샌다.
    for i in range(n):
        # 해당 선수 기록 범위 내에 none이 하나라도 있으면 제외
        if None in players[i][:i] + players[i][i+1:]:
            continue
        answer += 1

    return answer
