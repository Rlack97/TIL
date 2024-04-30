from collections import defaultdict

# 닉네임 dict
dictionary = defaultdict(int)

# 별칭 set
asterisk = set()

n = int(input())
for _ in range(n):
    # 닉네임 입력 받음
    nickname = input()
    f = False

    for i in range(1,len(nickname)+1):
        # 닉네임에서 앞에서 한글자씩 잘라서 별칭 생성
        tmp = nickname[:i]

        # 플래그가 있으면 스킵 (이미 별칭 등록함)
        # 별칭 또는 닉네임 사전에 겹치는 값이 없으면 그대로 출력
        if not f and tmp not in asterisk and tmp not in dictionary:
            # 별칭이 리스트에 없으면 출력하고 플래그 성립 (별칭 생성)
            print(tmp, end='')
            f = True

        # 가능한 모든 문자열은 모아둠. 이후 문자열의 별칭이 될 수 없다.
        asterisk.add(tmp)
    dictionary[nickname] += 1 
   
    # 플래그가 없으면 (가능한 별칭이 없으면)
    if not f:
        # 딕셔너리에 같은 닉네임의 수만큼 뒤에 숫자 추가
        if dictionary[nickname] >= 2:
            print(nickname + str(dictionary[nickname]), end='')
        else:
            print(nickname, end='')

    print()
