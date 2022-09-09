1. 무엇이 중복일까

   ```python
   def duplicated_letters(word):
       answer = set()
       for letter in word:
           if word.count(letter) != 1:
               answer.add(letter)
       return answer
   ```
   
2. 소대소대

   ```python
   def low_and_up(word):
       newword = ''
       for a in range(len(word)):
           if a % 2 == 0:
               newword += word[a].lower()
           else:
               newword += word[a].upper()
       return newword
   ```

3. 솔로 천국 만들기

```python
def lonely(numlist):
    solo = []
    for n in range(len(numlist)-1):
        if numlist[n] == numlist[n+1]:
            continue
        else:
            solo.append(numlist[n])
    solo.append(numlist[len(numlist)-1])
    return solo
```

