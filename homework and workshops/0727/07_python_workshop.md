1. pip

   ```python
   (1) faker 라는 파이썬 패키지를 설치하는 명령어입니다.
   (2) Git bash에서 실행해야 한다
   ```
   
2. basic usages

   ```python
   1. faker 패키지의 Faker 모듈을 불러오기 위한 코드이다
   2. Faker는 클래스, fake는 Faker의 인스턴스이다.
   3. name()은 fake의 메서드이다.
   ```
   
3. Localization

```python
def __init__(self,Locale):
    pass
```

4. Seeding th Generator

```python
1.
#1 이진호
#2 강은주
반복 실행했을 때 같은 결과를 출력하는 것으로 보아
Faker라는 클래스에 특정 시드를 부여해 시드값이 변하지 않는 한 처음 정해진 랜덤값이 유지되게 하는 메서드

2.
#1 이진호
#2 박종수

#2가 실행 시마다 바뀌는 것으로 보아
하나의 인스턴스에 시드를 부여해 해당 결과값을 고정해두는 메서드
```

