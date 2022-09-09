1. Type Class

   ```py
   int
   str
   list
   dict
   tuple
   set 등이 있다.
   ```

2. Magic Method

   ```python
   __init__ : 인스턴스가 생성될 때 자동으로 호출되는 메서드 (생성자)
   __del__ : 인스턴스가 삭제될 때 자동으로 호출되는 메서드 (소멸자)
   __str__ : 입력 받은 객체의 문자열 형태로 반환
   __repr__ : 입력 받은 객체의 '형태 그대로' 문자열로 반환 ????
   ```

3. Instance Method

   ```python
   .upper() = 문자열을 전부 대문자로 변환
   .append(X) = 리스트에 요소 x를 추가
   .Pop() = 리스트의 맨 오른쪽 항목을 반환 후 제거
   .count(x) = 리스트 안의 x의 개수를 반환
   ```

4. 오류의 종류

```python
ZeroDivisionError : 0으로 수를 나누려고 할 때
NameError : 접근 가능한 이름공간에 해당하는 이름이 없을 때
TypeError : 연산자를 사용한 객체 간 타입 불일치, argument가 누락되었을 때, argument의 개수가 초과되었을 때, argument의 type이 기준에 맞지 않았을 때
IndexError : 인덱스가 존재하지 않거나 범위를 벗어났을 때
KeyError : 해당 키가 존재하지 않는 경우
ModuleNotFoundError : 모듈이 없을 때
ImportError : 모듈은 있으나 존재하지 않는 클래스 혹은 함수를 가져오려 할 때
```
