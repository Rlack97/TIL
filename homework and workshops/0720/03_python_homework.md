1. built -in 함수

   ```python
   bool()
   complex()
   format()
   len()
   list()
   print()
   map()
   ```
   
2. 홀수만 담기

   ```python
   numbers = list(range(1,51))
   odd_numbers = numbers[0:49:2]
   print(odd_numbers)
   ```
   
3. 반복문으로 네모 출력

   ```python
   n = 5
   m = 9
   for i in range(1,m):
   	print ('*'*n)
   ```

4. 조건 표현식

   ```python
   temp = 36.5
   print('입실 불가') if temp>=37.5 else print('입실 가능')
   ```
   
5. 정중앙 문자
   ```python
   Word = input()
   def get_middle_char(char):
       k = len(char)
       if k % 2 == 0:
           print(char[int((k/2)-1)], end ='')
           print(char[int(k/2)])
       else :
           print(char[k//2])
           
   get_middle_char(Word)
   ```
