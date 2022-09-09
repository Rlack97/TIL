1. Circle 인스턴스 만들기

   ```py
   class Circle:
       pi = 3.14
   
       def __init__(self,r,x,y):
           self.r = r
           self.x = x
           self.y = y
   
       def area(self):
           return Circle.pi*self.r*self.r
   
       def circumference(self):
           return 2*Circle.pi*self.r
   
       def center(self):
           return (self.x, self.y)
   
   
   c = Circle(3,2,4)
   print(c.area())
   print(c.circumference())
   ```
   
   
   
2. Dog와 Bird는 Animal이다

   ```python
   class Dog(Animal):
       
       def__init__(self,name):
           super().__init__(name)
           
   	def run(self):
           print(f'{super().name}! 달린다!')
   
       def bark(self):
           print(f'{super().name}! 달린다!')
           
   class Bird(Animal):
       
       def__init__(self,name):
           super().__init__(name)
           
   	def fly(self):
           print(f'{super().name}! 푸드덕!')
   ```
   
3. Module Import

   ```python
   a : fibo 
   b : fibo_recursion
   c : recursion()
   ```
