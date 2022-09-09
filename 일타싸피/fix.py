if order == 1:
    if whiteBall_x <= targetBall_x and whiteBall_y <= targetBall_y:
        # 1사분면
        for i in [2,4]:
            flag = 0
            balls[i][0],balls[i][1] = ex, ey
            if whiteBall_x <= ex and whiteBall_y <= ey:
                E_width = abs(ex - whiteBall_x)
                E_height = abs(ey - whiteBall_y)

                # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
                #   - 1radian = 180 / PI (도)
                #   - 1도 = PI / 180 (radian)
                # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
                E_radian = math.atan(E_width / E_height) if E_height > 0 else 0
                E_angle = (180 / math.pi * radian) - (180 / math.pi * E_radian)
                # distance: 두 점(좌표) 사이의 거리를 계산
                E_distance = math.sqrt(E_width**2 + E_height**2)

                if E_distance * math.sin(E_angle) < 2*r:
                    flag = 1
                    break
        if flag == 1:
            continue
            

    elif whiteBall_x >= targetBall_x and whiteBall_y <= targetBall_y:
            # 2사분면
        for i in [2,4]:
            flag = 0
            balls[i][0],balls[i][1] = ex, ey
            if whiteBall_x >= ex and whiteBall_y <= ey:
                E_width = abs(ex - whiteBall_x)
                E_height = abs(ey - whiteBall_y)

                # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
                #   - 1radian = 180 / PI (도)
                #   - 1도 = PI / 180 (radian)
                # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
                E_radian = math.atan(E_width / E_height) if E_height > 0 else 0
                E_angle = (180 / math.pi * radian) - (180 / math.pi * E_radian)
                # distance: 두 점(좌표) 사이의 거리를 계산
                E_distance = math.sqrt(E_width**2 + E_height**2)

                if E_distance * math.sin(E_angle) < 2*r:
                    flag = 1
                    break
        if flag == 1:
            continue

    elif whiteBall_x >= targetBall_x and whiteBall_y >= targetBall_y:
            # 3사분면
        for i in [2,4]:
            flag = 0
            balls[i][0],balls[i][1] = ex, ey
            if whiteBall_x >= ex and whiteBall_y >= ey:
                E_width = abs(ex - whiteBall_x)
                E_height = abs(ey - whiteBall_y)

                # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
                #   - 1radian = 180 / PI (도)
                #   - 1도 = PI / 180 (radian)
                # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
                E_radian = math.atan(E_width / E_height) if E_height > 0 else 0
                E_angle = (180 / math.pi * radian) - (180 / math.pi * E_radian)
                # distance: 두 점(좌표) 사이의 거리를 계산
                E_distance = math.sqrt(E_width**2 + E_height**2)

                if E_distance * math.sin(E_angle) < 2*r:
                    flag = 1
                    break
        
        if flag == 1:
            continue

    elif whiteBall_x <= targetBall_x and whiteBall_y >= targetBall_y:
            # 4사분면
        for i in [2,4]:
            flag = 0
            balls[i][0],balls[i][1] = ex, ey
            if whiteBall_x <= ex and whiteBall_y >= ey:
                E_width = abs(ex - whiteBall_x)
                E_height = abs(ey - whiteBall_y)

                # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
                #   - 1radian = 180 / PI (도)
                #   - 1도 = PI / 180 (radian)
                # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
                E_radian = math.atan(E_width / E_height) if E_height > 0 else 0
                E_angle = (180 / math.pi * radian) - (180 / math.pi * E_radian)
                # distance: 두 점(좌표) 사이의 거리를 계산
                E_distance = math.sqrt(E_width**2 + E_height**2)

                if E_distance * math.sin(E_angle) < 2*r:
                    flag = 1
                    break
        if flag == 1:
            continue

targetBall_x = balls[1][0]
targetBall_y = balls[1][1]

# width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
width = abs(targetBall_x - whiteBall_x)
height = abs(targetBall_y - whiteBall_y)

# radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
#   - 1radian = 180 / PI (도)
#   - 1도 = PI / 180 (radian)
# angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
radian = math.atan(width / height) if height > 0 else 0
angle = 180 / math.pi * radian