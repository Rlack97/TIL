1. Python 예약어

   ```python
   import keyword
   keywork.kwlist
   ```

   ```python
   'False', 'None','True', '__peg_parser__','and','as','assert','async',
   'await','break','class','continue','def','del','elif','else','except',
   'finally','for','from','global','if','import','in','is','lambda',
   'nonlocal','not','or','pass','raise','return','try','while','with',
   'yield'
   ```

2. 실수 비교 

   ```python
   import math
   num1 = 0.1 * 3
   num2 = 0.3
   math.isclose(num1,num2)
   ```

   ```python
   num1 = 0.1 * 3 
   num2 = 0.3
   print(abs(num1-num2) <= 1e-10)
   ```

3. 이스케이프 시퀀스

   1. '\n'
   2. '\t'
   3. '\\\\'

4. String Interpolation

   ```python
   name = '철수'
   print(f'안녕, {name}야')
   ```

5. 형 변환
   * `int('3.5')`

6. 네모 출력

   ```python
   n, m = 5, 9
   print(('*' * n + '\n') *m)
   ```

7. 이스케이프 시퀀스 응용

   ```python
   print('''
   "파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다." \n 나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'
   ''')
   ```

   

8. 근의 공식

   ```python
   R1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
   R2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
   ```

분모/분자끼리는 괄호로 묶지 않으면 순서가 달라지는 것에 주의
