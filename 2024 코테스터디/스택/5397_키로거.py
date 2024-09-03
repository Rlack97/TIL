import sys
input = sys.stdin.readline

N = int(input())

for n in range(N):
    keylog = str(input()).rstrip()
    
    """
    백스페이스 = '-'
    화살표 입력 = '<' 또는 '>'
    커서가 맨 뒤가 아닐때는 커서 위치에 키 삽입
    뒤 글자들은 한칸씩 밀림
    
    커서를 기준으로 '왼쪽 글자 스택'과 '오른쪽 글자 스택'을 생성하면
    하나의 스택에서 중간에 값을 집어넣는 연산으로 인해 발생하는
    시간초과 이슈를 해결 가능
    
    """

    l_stack = []
    r_stack = []

    for key in keylog:
        if key == "<":
            # 왼쪽에 있던 맨 뒤 글자가 커서 오른쪽 맨 앞이 됨
            if l_stack:
                r_stack.append(l_stack.pop())
        elif key == ">":
            # 오른쪽에 있던 맨 앞 글자가 커서 왼쪽 맨 뒤가 됨
            if r_stack:
                l_stack.append(r_stack.pop())

        elif key == "-":
            # 왼쪽에 있던 맨 뒤 글자가 사라짐
            if l_stack:
                l_stack.pop()

        else:
            # 커서 왼쪽에 값이 들어감
            l_stack.append(key)
    
    # 오른쪽 스택은 쌓은 순서가 역순이므로 뒤집어서 합침
    r_stack.reverse()
    password = l_stack + r_stack

    print(*password, sep="")

    
