## 이름 짓기

#### 클래스 이름 

* 파스칼 케이스
  * 각 어절의 맨 앞의 글자를 대문자로
    *  ChanBin
    *  MyList

#### 함수 혹은 변수 이름

* 카멜 케이스 
  * 두 번째 어절의 글자를 대문자로
    * chanBin 
    * myList

---

## 실제 활용

```py
class Dog1:
    
    kind = 'canine'              # 클래스 변수
    
    def __init__(self,name):
        self.name = name         # 인스턴스 변수
```

```py
print('-Dog1-')
chanbin_dog = Dog1('Atto')
print('-Dog1-')
ej_dog = Dog1('Zangha')
```

```py
# 인스턴스 변수에의 접근
print(chanbin_dog.name)
print(ej_dog.name)
# 클래스 변수에 접근
print(chanbin_dog.kind)
print(ej_dog.kind)
```

------------------------------------------------------------------------------------------------------------------------------------------------------

```py
class Cat:
    tricks = []      #값을 추가할 빈 리스트
    
    def __init__(self, name):
        self.name = name
        
    def add_trick(self, trick):
        self.tricks.append(trick)    # 클래스 변수를 인스턴스에서 활용하기 위해서는
                                     # self.이 앞에 붙어있어야 한다
```

```py
hb_cat1 = Cat('milk')
hb_cat2 = Cat('cream')
```

```python
print(hb_cat1.name)
print(hb_cat2.name)

hb_cat1.add_trick('hi')
hb_cat2.add_trick('hello')

print(hb_cat1.tricks)           # tricks는 클래스 변수이므로,
print(hb_cat2.tricks)           # hi와 hello 전부 삽입되어 있음

#['hi','hello']
```

---

```python
# 인스턴스 별 입력값을 구분하면, 인스턴스 변수로 선언해야 한다

class Tiger:
    def __init__(self, name):
        self.name = name
        self.tricks = []         # 값을 따로 넣을 빈 리스트
        
 	def add_trick(self,trick):
        self.tricks.append(trick)    # self.을 사용해서 인스턴스 변수 호출
```

```python
my_tiger = Tiger('Ccoby')
your_tiger = Tiger('싸버지')
```

```python
print(my_tiger.name)
print(your_tiger.name)

my_tiger.add_trick('어흥')
your_tiger.add_trick('크아앙')

print(my_tiger.tricks)              # ['어흥'] 
print(your_tiger.tricks)            # ['크아앙']

# 이번에 tricks는 인스턴스 변수이므로
# '어흥'과 '크아앙'이 따로 기억되어 있음
```

---

```python
#절차 지향 = 함수
def greeting(name):
    return f'hello, {name}!'

print('밥')  # hello, 밥!

#객체 지향 = 클래스
class Person:
	def __init__(self,name):
        self.name = name
        
	def greeting(self):
        return f'hello, {self.name}!'
```

```python
my_name = Person('지혜')
print(my_name.greeting())    # hello, 지혜!
```

```python
class : Greeting:
    def __init__(self,name):
        self.name = name
        
	def hello:
        return f'hello, {self.name}!'
	def hihi:
        return f'hihi, {self.name}!'
    def bye:
        return f'bye, {self.name}!'
    
my_name = Greeting('nem')
print(my_name.hello())
print(my_name.hihi())
print(my_name.bye())
    
```





Q. 객체지향이 뭐냐? (면접)

A. 개발자의 관점에서 편리하게 프로그래밍이 가능한 문법



SRP(단일 책임 원칙) - 클래스별 관리, 분리, 변경이 편함