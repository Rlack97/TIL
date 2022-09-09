1. 평균 점수 구하기

   ```python
   def get_dict_avg(X):
       x = 0
       y = 0
       for a,b in X.items():
           x += b
           y += 1
       return(x/y)
   ```
   
2. 혈액형 분류하기

   ```python
   def count_blood(x):
       A = 0
       B = 0
       O = 0
       AB = 0
       for P in x:
           if P == 'A':
               A+=1
           elif P == 'B':
               B+=1
           elif P == 'O':
               O+=1
           elif P == 'AB':
               AB+=1
       T = {'A': A, 'B':B, 'O':O, 'AB':AB}
       return T
   ```

```py

```

