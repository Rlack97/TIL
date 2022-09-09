1. 세로로 출력하기

   ```python
   number = int(input())
   for N in range(1,number+1):
   	print(N)
   ```

2. 가로로 출력하기

   ```python
   number = int(input())
   for N in range(1,number+1):
   	print (N, end = ' ')
   ```
   
3. 거꾸로 세로로 출력하기

   ```python
   # range를 역순으로 되돌림
   number = int(input())
   for N in range(number,-1,-1):
       print(N)
   ```
   
4. 거꾸로 출력해 보아요

   ``` python
   number = int(input())
   for N in range(number,-1,-1):
       print(N, end = ' ')
   ```

5. N줄 덧셈

    ```python
    number = int(input())
    S_number = 0
    for N in range(1,number+1):
        S_number += N
    print(S_number)
    ```

6. 삼각형 출력하기

   ```py
   # 도전과제! 너무 어려우면 포기해도 됨
   # 힌트 : 이중 for문
   
   N = int(input())
   for i in range(1,N+1):
       for j in range(i,i+1):
           print(" "*(N-i) + "*"*i)
   ```

7. 중간값 찾기

   ```py
   numbers = list(map(int,input().split()))
   
   numbers.sort()
   print (numbers[len(numbers)//2])
   
   ------------
   
   #sort, len, sum 미사용 
   
   numbers = list(map(int,input().split()))
   
   def my_len(list):
       count = 0
       for a in list:
           count += 1
       return count
   
   K = my_len(numbers)
   
   def bubblesort(x):
   	for i in range(K-1):
       	for j in range(K-1):
               if x[j] > x[j+1]:
                   x[j], x[j+1] = x[j+1], x[j]
       return x
   	
   bubblesort(numbers)
   
   print(numbers[K//2])
   ```
   
   
