import random  # 랜덤 모듈 활용

print("================================")
print("        Battle Ship Game        ")
print("            START !!            ")
print("================================")

# 필요에 따라 추가적으로 함수를 만들어 자유롭게 활용할 수 있습니다.
# 각자의 해역에 배를 위치시키는 함수
def set_ship(index, sea):
    for K in range(index,index+3):
        sea[K-1] = 1

player_sea = [0] * 15  # 플레이어의 해역
player_attacked = [False] * 15  # 플레이어의 공격 위치 기록

computer_sea = [0] * 15  # 컴퓨터의 해역
computer_attacked = [False] * 15  # 컴퓨터의 공격 위치 기록

round = 1  # 게임 라운드

# 1. 게임 준비
while True:
    # 1-1) 플레이어의 배 시작 위치 고르기
    player_start = int(input("배를 위치시킬 시작점을 고르세요. : "))

    # 1-2) 범위를 벗어난 시작점을 고른 경우
    if player_start > 13 or player_start < 1 :
        print("-----해당 위치에는 배를 둘 수 없습니다.-----")
        continue

# 1-3) 컴퓨터의 배 시작 위치를 랜덤으로 지정합니다.
    computer_start = random.choice(range(1,14))

# 1-4) 플레이어와 컴퓨터의 해역에 각각 배 위치시키기
    set_ship(player_start, player_sea)
    set_ship(computer_start, computer_sea)
    break

# 2. 라운드 진행
while True:
    # 2-1) 플레이어 공격
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("<Information Board>")
    print(f"플레이어의 해역: {player_sea}")
    print(f"플레이어의 공격 기록: {player_attacked}")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    # 2-2) 플레이어의 공격 위치 선택
    while True:
        P_attack = int(input("공격할 위치를 선택하세요. : "))
        if P_attack > 15 or P_attack < 1 :
            print("해역의 범위에서 벗어난 위치를 선택하셨습니다. 다시 선택해 주세요.")
            continue
        elif player_attacked[P_attack-1] == True :
            print("이미 공격한 위치를 선택하셨습니다. 다시 선택해 주세요.")
            continue
        break
    
    # 2-3) 플레이어의 공격이 성공한 경우
    if computer_sea[P_attack-1] == True:
        print(f"<{round}라운드 결과!>")
        print(f"컴퓨터의 해역 : {computer_sea}")
        print(f"플레이어는 컴퓨터의 해역 {P_attack}번째 칸을 공격하였고, 컴퓨터의 배는 피격되었습니다.")
        print(f"게임이 종료되었습니다! {round}라운드 만에 플레이어의 승리입니다!")
        break
    # 2-4) 플레이어의 공격이 실패한 경우
    elif computer_sea[P_attack-1] == False:
        player_attacked[P_attack-1] = True

    # 2-5) 컴퓨터의 공격 위치 지정
    # 컴퓨터가 공격하지 않은 위치를 나타내는 리스트
    not_attacked = []
    for M in range(15):
        if computer_attacked[M] == False:
            not_attacked.append(M)

    C_attack = random.choice(not_attacked)
    # 2-6) 컴퓨터의 공격이 성공한 경우
    if player_sea[C_attack-1] == True:
        print(f"<{round}라운드 결과!>")
        print(f"플레이어는 컴퓨터의 해역 {P_attack}번째 칸을 공격하였으나, 공격에 실패하였습니다!")
        print(f"컴퓨터는 플레이어의 해역 {C_attack}번째 칸을 공격하였고, 플레이어의 배는 피격되었습니다.")
        print(f"게임이 종료되었습니다! {round}라운드 만에 컴퓨터의 승리입니다!")
        break
    # 2-7) 컴퓨터의 공격이 실패한 경우
    elif player_sea[C_attack-1] == False :
        computer_attacked[C_attack-1] = True
        print(f"<{round}라운드 결과!>")
        print(f"플레이어는 컴퓨터의 해역 {P_attack}번째 칸을 공격하였으나, 공격에 실패하였습니다!")
        print(f"컴퓨터는 플레이어의 해역 {C_attack}번째 칸을 공격하였으나, 공격에 실패하였습니다!")
        round += 1
