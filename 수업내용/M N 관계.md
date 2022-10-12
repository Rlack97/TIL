# M:N 관계

강의 주차: 14주차
유형: DB
작성일시: 2022년 10월 12일 오전 8:41

# 다대다 관계

### M:N

- 한 테이블의 N개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우
- 양쪽 모두에서 N:1 관계를 가짐

**의사와 환자간의 예약 시스템**

- 어떤 데이터베이스 모델이 필요한가?
- 일상의 예시들에 대한 데이터 흐름에 대한 고민

**용어**

- 타겟 모델
    - 관계 필드를 가지지 않은 모델
    - 게시글
- 소스 모델
    - 관계 필드를 가진 모델
    - 댓글

**N:1의 한계**

- 의사 및 환자간 예약 시스템을 구현
- 한 명의 의사에게 여러 환자가 예약 가능한 N:1모델을 설정
    - 각 환자가 서로 다른 의사에게 예약을 했다고 가정
    - 1번 환자가 두 의사 모두에게 방문하려고 한다면?
    - 동시에 예약이 가능한가?
        - 동일한 환자이지만 다른 의사에게 예약하기 위해서는 객체가 하나 더 필요함
        - 외래 키는 IntegerField이므로  (1,2)와 같이 여러 수를 넣는 것이 불가능
            - ⇒ 예약 테이블을 따로 만들어야 함
    

**중개 모델**

- 환자 모델의 외래 키를 삭제하고, 별도의 예약 모델을 새로 작성
- 예약 모델은 의사와 환자에 각각 N:1 관계를 가짐
    - 새로운 환자 예약은 3번째 예약 필드에만 값이 늘어남
    - 환자/의사.reservatioin_set.all() 을 통해 예약 정보를 조회 가능
        - 타겟 모델이 소스 모델을 참조하는, 역참조 형태

**다대다 모델**

- 환자 모델에 다대다 필드를 작성
    
    ```sql
    class Patient(models.Model):
        doctor = models.ManyToManyField(Doctor)
        name = models.TextField()
    
        def __str__(self):
            return f'{self.pk}번 환자 {self.name}'
    ```
    
- 다대다 모델은 외래키를 갖는 중개 테이블을 알아서 생성함.
    - 두 모델 중 어느 쪽이 다대다 필드를 갖는지는 상관 없지만,
    - 서로간의 참조/역참조 관계는 바뀌므로 주의
- 예약하기 (생성
    - patient2.doctors.add(doctor1)  - 참조 형태
    - doctor1.patient_set.add(patient1) - 역참조 형태
    - `.add()`를 사용
- 예약 취소하기(삭제)
    - patient2.doctors.remove(doctor1)  - 참조 형태
    - doctor1.patient_set.remove(patient1) - 역참조 형태
    - `.remove()`를 사용
- MtM 필드에서 related_named을 설정하면, 역참조 시 함수의 형태가 바뀜
    - doctor = models.ManyToManyField(Doctor, related_name=’patients’)
        - doctor1.patients.add(patient1)
        - doctor1.patients.remove(patient1)

**중개 모델을 직접 작성하는 경우**

- through 옵션을 통해 사용하려는 중개 테이블을 나타내는 모델을 지정 가능
- 일반적으로는 중개테이블에 추가 데이터를 사용해 다대다 관계와 연결하려는 경우

```sql
class Patient(models.Model):
    doctor = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
		doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
		patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
		symptom = models.TextField()
		reserved_at = models.DateTimeField(auto_now_add=True)

		def __str__(self):
        return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'
```

- 예약 생성
    
    ```sql
    #1 reservation 클래스를 통한 생성
    reservation1 = Reservation(doctor=doctor1, patient=patient1, symptom=’headache’)
    reservation1.save()
    
    #2 patient 객체를 통한 생성
    patient2.doctors.add(doctor1, through_defaults={'symptom':'flu'}
    # defaults 값은 딕셔너리 타입으로 입력
    ```
    

**정리**

- M:N 관계로 맺어진 두 테이블에는 변화가 없음
- 장고의 MTM 필드는 중개 테이블을 자동으로 생성
- MTM 필드는 두 필드 중 어디에 위치해도 상관없음
    - 필드 작성 위치에 따라 바뀌는 참조와 역참조 관계에 주의
- N:1은 완전한 종속관계였지만, M:N은 서로가 서로에게 관계하는 두 가지 형태로 표현 가능

### ManyToManyField

- (to, **options)
- 다대다 관계 설정 시 사용
- 하나의 필수 위치인자가 필요
- 모델 필드의 relatedmanager를 사용하여 관련 개체를 추가 제거 또는 생성할수 있음
    - add(), remove(), create(), clear()…
- 중계 테이블의 이름은 MTM 이름과 이를 포함하는 모델의 테이블 이름을 조합
    - `db_table` arguments를 사용하여 중개 테이블의 이름을 변경할 수도 있음

**MTM필드의 인자값**

1. related_name
    - 타겟모델이 소스모델을 참고할 때 사용할 매니저 네임
2. through
    - 중개 테이블을 직접 작성하는 경우
    - 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우 사용
3. symmetrical
    - 대칭
    - 기본값 = True
        - 한 쪽의 관계가 설정되면 그 반대의 관계도 추가가 됨
            - 1 → 2일때 2→1도 자동으로 추가됨
    - MTM필드가 동일한 모델을 가리키는 정의에서만 사용
        - 재귀적 참조
        
        ```sql
        class Person(models.Model):
        		friends = models.ManyToManyField('self')
        		# friends = models.ManyToManyField('self', symmetrical=False)
        		# 팔로우 개념, 비대칭적 관계
        ```
        

**Related Manger**

- N:1 또는 M:N 관계에서 사용 가능한 문맥
    - N:1 에서는 타겟 모델 객체만 사용가능
    - M:N 관계에서는 관련된 두 객체에서 모두 사용 가능
        - add(), remove(), create(), clear(), set() 등

## M:N (게시글-유저, 좋아요 기능)

- ManyToManyField 작성
    
    ```sql
    class Article(models.Model):
    		user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    		like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    		title...
    ```
    
    - 에러발생
        - 이미 N:1관계에서 article_set 매니저가 형성되어 있기 때문
        - 따라서 related_name을 새로 지정해 주어야 함
    
    ```sql
    class Article(models.Model):
    		user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    		like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    		title...
    ```
    
    - 에러 없이 생성이 진행됨
    - related manager 정리
        - article.user
        - user.article_set
        - article.like_users
        - user.like_articles

**구현**

```sql
# urls.py
		path('<int:article_pk>/likes/', views.likes, name='likes'),

#views.py
@require_POST
def likes(request, article_pk):
#		if request.user.is_authenticated:
				article = Article.objects.get(pk=article_pk)
				if article.like_users.filter(pk=request.user.pk).exists():
						article.like_users.remove(request.user)
						# 좋아요 취소
				else:
						article.like_users.add(request.user)
						# 좋아요 추가
				return redirect('articles:index')		
#		return redirect('accounts:login')
		

# templates/articles/index.html
<div>
	<form action = "{% url 'articles:likes' article.pk%}" method="POST">
		{%csrf_token%}
		{%if request.user in article.like_users.all%}
			<input type="submit" value="좋아요취소">
		{%else%}
			<input type="submit" value="좋아요">
		{%endif%}
	</form>
</div>
```

- `.exists()`
    - 쿼리셋에 결과가 포함되어 있으면 True, 그렇지 않으면 False
    - 특히 큰 쿼리셋에 있는 특정 개체의 존재와 관련된 검색에 유용

## M:N(유저-유저, 팔로우 기능)

### 프로필 페이지

- 자연스러운 팔로우 흐름을 위한 프로필 페이지를 먼저 작성

```sql
# urls.py
		path('profile/<username>/', views.profile, name='profile'),
# views.py
from dgango.contrib.auth import get_user_model

def profile(request, username):
		User = get_user_model()
		person = User.objects.get(username=username)
		context = {
				'person':person,
		}
		return render(request, 'accounts/profile.html', context)
```

- 템플릿

```sql
{% extends 'base.html' %}

{% block content %}
<h1>{{ person.username }}님의 프로필</h1>

<hr>

<h2>{{ person.username }}s 게시글</h2>
{% for article in person.article_set.all %}
    <div>{{article.title}}</div>
{% endfor %}

<hr>

<h2>{{ person.username }}s 댓글</h2>
{% for comment in person.comment_set.all %}
    <div>{{comment.content}}</div>
{% endfor %}

<hr>

<h2>{{ person.username }}s 좋아요한 게시글</h2>
{% for article in person.like_articles.all %}
    <div>{{article.title}}</div>
{% endfor %}

<hr>

<a href="{% url 'articles:index' %}">back</a>

{% endblock content %}
```

- 프로필로 이동하는 하이퍼링크

```sql
# base.html
<a href ="{% url 'accounts:profile user.username%}"> 내 프로필 </a>

# index.html 등
<p>
	작성자 : <a href="{% url 'accounts:profile article.user.username%}">{{article.user}}</a>
</p>
```

### 팔로우

- 모델 변경

```sql
# accounts/models.py
class User(AbstractUser):
		followings = modles.ManyToManyField('self',symmetrical=False, related_name='followers')
```

- url 및 함수 구현

```sql
# urls.py
		path('<int:user_pk>/follow/', views.follow, name='follow'),

@require_POST
# views.py
def follow(request, user_pk):
		if request.user.is_authenticated:

			User = get_user_model()
			person = User.objects.get(pk=user_pk)
			if person != request.user:
	
			# 언팔로우하기
			if person.followers.filter(pk=request.user.pk).exists():
					person.followers.remove(request.user)
	
			# 팔로우하기
			else:
					person.followers.add(request.user)
			return redirect('accounts:profile', person.username)
		return redirect('accounts:login')
```

- 프로필 페이지의 팔로잉/팔로워 수 & 팔로우, 언팔로우 버튼 작성

```sql
#profile.html

<div>
	<div>
		팔로잉 : {{ person.followings.all | lentgh}} / 팔로워 : {{ person.followers.all | lentgh }}
	</div>
	
	{% if request.user != person %}
		<div>
			<form action="{% url 'accounts:follow' person.pk %}" method="POST">
				{%csrf_token%}
				{%if request.user in person.followers.all%}
					<input type="submit" value="Unfollow">
				{% else %}
					<input type="submit" value="follow">
				{% endif %}
			</form>
		</div>
	{% endif %}
</div>
```