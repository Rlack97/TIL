1. 모음은 몇 개나 있을까?

   ```python
   def count_vowels(X):
      k = X.count('a') + X.count('i') + X.count('o') + X.count('u') + X.count('e')
      return k
   ```

   ```py
   def count_vowels(word):
       vowles = ['a','e','i','o','u']
       cnt = 0
       for vowel in vowels:
       	cnt += word.count(vowel)
       return cnt
   ```

   

2. 문자열 조작

   ```python
   4. 지정하지 않을 경우 공백을 제거합니다.
   ```

3. **정사각형**만 만들기

   ```python
   def only_square_area(A,B):
       k = []
       for a in A:
       	for b in B:
               if a == b:
   		    	k.append(a*b)
       return k
   
   ```
