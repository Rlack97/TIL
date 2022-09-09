a,b,c = map(int,input().split())
total = [a,b,c]
total.sort()
if a == b == c:
    print (10000 + a*1000)
elif a == b or b == c or c == a:
    print (1000 + total[2]*100)
elif a != b and b != c and a != c:
    print (total[2]*100)    
