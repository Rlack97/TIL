# 입력을 받습니다.
n, m = map(int, input().split())
buses = [list(map(int, input().split())) + [0] for _ in range(m)]
# [t, p, c] = [도착시간,정차시간,정류장 위치]

# 정차 중인 버스 수, 현재 시간, 정차시간이 끝난 첫 번째 버스,  현재 처리중인 버스
cn, ct, fin, index = 0, 0, 0, 0

while index < m or any(b[1] > 0 for b in buses):
    # 시간 증가
    ct += 1

    for i in range(fin, fin + cn):
        # 현재 정차하고 있는 버스들의 정차시간 감소
        buses[i][1] -= 1

        if buses[fin][1] <= 0 and (i == fin or buses[i][1] <= 0):
            fin += 1
            cn -= 1
            # 뒤에 버스들의 정차 시간이 끝나도 첫 번째 정차 중인
            # 버스의 타이머가 끝날 때까지 대기 후 변수 조정

    while cn < n and index < m and ct >= buses[index][0]:
        # 버스 수가 최대 정차 수보다 작고 현재 시간이 다음 버스가 들어올 수 있으면
        if cn > 0 and buses[fin + cn - 1][2] == n:
            break
            # 직전 버스가 정류소의 맨 끝에 있으면 못 들어감
        if cn == 0:
            buses[index][2] = 1  # 정류소에 버스가 없으면 1번 위치로
        else:
            buses[index][2] = buses[fin + cn - 1][2] + 1
            # 버스가 있다면 그 버스의 바로 뒤로
        index += 1
        cn += 1

print(buses[m - 1][2])
