# 아래에 답안을 작성해 주세요.
ports = list(range(1,16)) # 1번부터 15번 선착장 리스트
boat = {4,8,9,15}         # 보트가 있는 곳

for a in ports:
    if a in boat:
        ports[a-1] = True
    else:
        ports[a-1] = False
        
print (ports)
