cnt = 1
total_salt = 0
total_water = 0

while True : 
    A = list(map(str,input(f'{cnt}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오 : ').split()))
    if A == ['Done']:
        break
    a = int(A[0].strip('%'))
    b = int(A[1].strip('g'))
    total_salt += (a*b)/100
    total_water += b
    cnt += 1 
    if cnt > 5:
        break
        
    P = '%10.1f'%(round(total_salt/total_water*100,1))
    Q = '%10.1f'%(round(total_water,1))
    
print (f'{P}%'.strip(), end=' ')
print (f'{Q}g'.strip())