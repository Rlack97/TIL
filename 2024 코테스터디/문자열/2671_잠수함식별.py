# 0320

import re
# 정규 표현식 사용
# 특정 패턴이 1회 이상 반복되는 확인 할 수 있는 메타 문자인  +  사용
s = input()
p = re.compile('(100+1+|01)+')
m = p.fullmatch(s)
if m:
    print("SUBMARINE")
else:
    print("NOISE")
