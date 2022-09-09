1. 위치 인자와 키워드 인자

   ```python
   4번.
   키워드 인자 뒤에 위치인자는 사용 불가능하기 때문입니다.
   ```
   
2. 가변 인자 리스트

   ```python
   def my_avg(*x):
       z = 0
       c = 0
       for y in x:
   	    z += y
       	c += 1
       return z/c
   ```
   
3. 반환값

   ```python
   my_func(a,b)에는 return 이 포함되어 있지 않으므로, 
   10이 출력되지만 result에는 값이 저장되지 않습니다.
   따라서 result의 값은 None입니다.
   ```
   
4. 이름 공간

   ```python
   Local -> Enclosed -> Global -> Built-in
   ```
   
5. 매개변수와 인자, 그리고 반환
   ```python
   4
   ```

6. 재귀함수

```python
#재귀 함수는 반복문에 비해 변수의 수를 줄일 수 있다는 장점이 있습니다.

def B(x):
    if x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        return B(x-1) + B(x-2)
   # x 하나로 끝나는 피보나치 재귀함수에 비해

def A(x):   
    a, b = 0, 1
    for i in range(x):       # 반복문은 빈 값인 a,b를 지정해 값을 저장해줘야 합니다
        a, b = b, a+b
    return a
```
