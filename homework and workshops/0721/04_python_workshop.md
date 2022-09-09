1. 간단한 N의 약수

   ```python
   N = int(input())
   result = []
   for a in range(1,N+1):
       if N % a == 0:
           result.append(a)
   
   print(result)
   ```
   
2. List의 합 구하기

   ```python
   def list_sum(INPUTLIST):
       a = 0
       for i in INPUTLIST:
           a  = a + int(i)
       return(a)
   ```
   
3. Dictionary로 이루어진 List의 합 구하기

   ```python
   def dict_list_sum(T):
       a = 0
       for i in T:
       	a += i['age']
       return(a)
   ```
   
4. 2차원 리스트의 전체 합 구하기

   ``` python
   def all_list_sum(X):
       k = 0
       for a in X:
           for i in a:
           	k += i
       return k
   ```

5. 숫자의 의미

    ```python
    def get_secret_word(alist):
    	k = ''
        for a in alist:
    		k += chr(a)
        return k
    ```
    
6. 내 이름은 몇일까?

   ```py
   def get_secret_number(word):
       k = 0
       for a in word:
       	k += ord(a)
       return k
   ```
   
7. 강한 이름

   ```py
   def get_strong_word(a,b):
       A = get_secret_number(a)
       B = get_secret_number(b)
       if A > B:
           return a
       elif A < B :
           return b
       elif A == B:
           return a,b
   ```
   
   
