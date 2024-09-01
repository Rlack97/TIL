def calculate_spiral_value(r, c):
    #오른쪽으로 이동
    if r >= c and r >= -c:
        layer = r
        return (2 * layer + 1) ** 2 - (layer - c)
    
    # 위로 이동
    elif r > c and r < -c:
        layer = -c
        return (2 * layer + 1) ** 2 - 3 * layer + r
    
    #왼쪽으로 이동
    elif r <= c and r <= -c:
        layer = -r
        return (2 * layer + 1) ** 2 - 5 * layer - c
    
    #아래로 이동
    else:
        layer = c
        return (2 * layer + 1) ** 2 - 7 * layer - r

def print_spiral(r1, c1, r2, c2):
    grid = []
    max_len = 0
    
    for r in range(r1, r2 + 1):
        row = []
        for c in range(c1, c2 + 1):
            value = calculate_spiral_value(r, c)
            row.append(value)
            max_len = max(max_len, len(str(value)))
        grid.append(row)
    
    for row in grid:
        for value in row:
            print(f"{value:>{max_len}}", end=" ")
        print()

import sys
input = sys.stdin.readline
r1, c1, r2, c2 = map(int,input().split())
print_spiral(r1, c1, r2, c2)