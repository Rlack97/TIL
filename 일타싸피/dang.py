#하얀공 
wx,wy = int(input())
#목적공
mx,my = int(input())
holes = [[0,0],[127,0],[254,0],[0,127],[127,127],[254,127]]


# 공 직경 = 5.73, 반지름 = 2.865
# 점 사이의 거리 = 피타고라스
# 점 사이의 각도 = 삼각함수, 라디안


# 1. 하얀공과 목적공의 위치관계 탐색.
if mx >= wx and my >= wy:
    base = 90
elif mx > wx and my < wy:
    base = 180
elif mx <= wx and my <= wy:
    base = 270
elif mx < wx and my > wy:
    base = 360

# 2. 목적구와 홀 간의 거리가 가장 가까운 홀 위치 구하기.

close = []
for h in holes:
    k = (abs(h[1]-mx)**2 + abs(h[2]-my)**2)**(1/2)
    close.append(k)

hole = holes.index(min(close))+1

# 3. 삼각함수를 사용해서 세타 구하기
import math
r = 2.865
hx = hole[0]
hy = hole[1]

a = abs(mx-hx)
b = abs(my-hy)

if mx >= hx:
    crashx = hx+2*r*(a/(a**2+b**2)**(1/2))
else:
    crashx = hx-2*r*(a/(a**2+b**2)**(1/2))

if my >= hy:
    crashy = hy+2*r*(b/(a**2+b**2)**(1/2))
else:
    crashy = hy-2*r*(a/(a**2+b**2)**(1/2))


# 기준값에서 계산. 사분면마다 방식이 바뀜

seth = math.atan2(abs(hy-crashy),abs(hx-crashx))
if base == 90 or base == 270:
    if abs(crashx-wx) >= abs(crashy-wy):
        angle = base - math.degrees(seth)
    else:
        angle = base-90 + math.degrees(seth)

if base == 180 or base == 360:
    if abs(crashx-wx) >= abs(crashy-wy):
        angle = base-90 + math.degrees(seth)
    else:
        angle = base - math.degrees(seth)
        

power = 70