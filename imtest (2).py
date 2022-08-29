T = int(input())
for tc in range(1, T+1):
    N, Kmin, Kmax = map(int, input().split())
    Escore = list(map(int, input().split()))
    Sscore = sorted(Escore)
    answer_list = []

    for i in range(Sscore[0], Sscore[-1]):
        T1 = i+0.5
        for k in range(i, Sscore[-1]):
            T2 = k+0.5
            A, B, C = 0, 0, 0
            for t in Sscore:
                if t < T1:
                    C += 1
                elif T1 <= t < T2:
                    B += 1
                else:
                    A += 1
            D = [A, B, C]
            if Kmin <= C <= Kmax and Kmin <= B <= Kmax and Kmin <= A <= Kmax:
                answer_list.append(max(D)-min(D))
            else:
                continue

    if answer_list == []:
        answer = -1
    else:
        answer = min(answer_list)

    print('#{} {}'.format(tc, answer))