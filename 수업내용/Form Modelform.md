# Form/Modelform

강의 주차: 9주차
복습: No
유형: Django
작성일시: 2022년 9월 6일 오전 8:45

## Django Form

- 서버에 들어오는 데이터에 대한 유효성 검증이 필요함.
- 서버에 대한 요청이 비정상적이거나 악의적인 경우에 대한 대처 필요
- django form을 통해 쉽고 간편하게 진행 가능
    - form과 같은 유효성 검사를 단순화하고 자동화할 수 있는 기능을 제공
- django form이 처리하는 작업
    - 렌더링을 위한 데이터 준비 및 재구성
    - 데이터에 대한 HTML forms생성
    - 클라이언트로부터 받은 데이터 수신 및 처리

### django form class

- form class 선언
    - 모델 클래스와 비슷한 이름의 필드 타입이 많음
    - model과 마찬가지로 상속을 통해 선언받는다. `(forms.Form)`
- 작업순서
    1. 앱 폴더에 forms.py를 생성 후 클래스 선언
        
        ```jsx
        from django import forms
        
        class ArticleForm(forms.Form):
        	title = forms.Charfield(max_length=10) 
        # forms에서 charfield의 maxlength는 필수입력값이 아님
        	content = forms.Charfield()
        ```
        
    - Textfield는 존재하지 않음.
    - 모델과 유사하게 사용하려면 어떻게 할까?
    1. articles/views.py 에서 ‘new’ 페이지 수정
        
        ```jsx
        from .forms import ArticleForm
        
        def new(request):
        	form = ArticleForm()
        	context = {'form':form,}
        	return render(request, 'articles/new/html', context)
        ```
        
    2. ‘new.html’ (템플릿) 업데이트
        
        ```jsx
        ...
        <form action ="{%url 'articles:create%}" method="POST">
        	{%csrf_token%}
        	{{form.as_p}}
        	<input type="submit">
        </form>
        ...
        ```
        

→ 출력 확인

- {{form}} 하나로 input과 label태그가 전부 자동 작성되어 있음
- 태그의 속성 값 역시 자동 설정

### form 렌더링 옵션

- label & input 쌍에 대한 3가지 출력 옵션
    1. `{{form.as_p}}`
        - 각 필드가 단락(p태그)로 감싸져서 렌더링
    2. `{{form.as_ul}}`
        - 각 필드가 목록 항목 (li태그)로 감싸져서 랜더링
    3. `{{form.as_table}}`
        - 각 필드가 테이블 행(tr태그)으로 감싸져서 렌더링
- Django의 2가지 input 요소 표현 (forms.py)
    - form  fields
        - `forms.Charfield()`
        - 입력에 대한 유효성 검사 로직
    - Widget
        - `forms.Charfield(widget=forms.Textarea)`
        - input 요소의 단순한 출력 부분을 담당

### Widgets

- Django의 HTML 인풋 요소의 표현을 담당
- 렌더링을 처리하는 부분이며, 유효성 검증과 관계가 없음
- 공식문서를 참고하여 종류를 파악하면 됨

## Django ModelForm

- forms과 model과 중복되는 부분들이 많음
- modelform을 사용하면 더 쉽게 form을 작성할 수 있음
- View 함수에서 사용

### modelform 선언

- `article/forms.py` 에서 작성
- 정의한 modelform 클래스 안에 Meta 클래스를 선언
- 어떤 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta에 지정
    
    ```jsx
    from django import forms
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
    
    	class Meta:
    		model = Article
    		fields='__all__'
    ```
    
    - meta 클래스
        - 모델form의 정보를 작성하는 곳
        - meta 클래스의 model속성이 참조할 모델을 구성
        - 참조하는 모델에 정의된  field 정보를 form에 적용
        - `__all__`을 사용하는 것으로 모든 필드를 포함할 수 있음.
        - `exclude =` 를 사용하여 모델에서 포함하지 않는 필드만 지정 가능
    - 정의
        - 메타데이터 = 데이터를 표현하기 위한 데이터
        - 사진 데이터
        - 사진 데이터의 데이터 = 촬영 시각, 렌즈, 조리개 값 등
- 함수의 참조와 반환
    - 참조 = 함수명
    - 반환 = 함수명()
    - 참조를 사용하는 이유는 타 함수에서 필요할 때 해당 함수를 이용하게 하기 위함.

### modelform with view functions

- create 페이지
    - 유효성 검사를 통과하면
        - 데이터 저장 후 상세 페이지로 리다이렉트
    - 통과하지 못하면 작성 페이지로 리다이렉트
        
        ```jsx
        def create(request):
        	form = ArticleForm(request.POST)
        	if form.is_valid():
        		article = form.save
        		return redirect('article:detail', article.pk)
        	retrun redirect('articles:new')
        ```
        
- is_valid() 매서드
    - 유효성 검사를 실행하고, 데이터가 유효한지의 여부를 boolean으로 반환
    - 데이터 유효성 검사를 보장하기 위한 많은 테스트들을 간소화
- form 인스턴스의 errors 속성
    - is_valid() 값이 False인 경우 errors 속성에 값이 작성되는데, 
    유효성 검증을 실패한 원인이 딕셔너리 형태로 저장됨
    - 다음 구조로 코드를 작성하면 실패 결과 메세지가 출력 가능
        
        ```jsx
        def create(request):
        	form = ArticleForm(request.POST)
        	if form.is_valid():
        		article = form.save
        		return redirect('article:detail', article.pk)
        	context = {'form':form,}
        	return render(request, 'articles/new.html'. context)
        ```
        
- save() 메서드
    - form 인스턴스에 바인딩 된 데이터를 통해 데이터베이스 객체를 만들고 저장
    - ModelForm의 하위 클래스는 키워드 인자 instance 여부를 통해 생성할지 수정할지 결정
        - 제공되지 않는다면 save는 지정된 모델의 새 인스턴스를 만듦 → CREATE
        - 제공되면 해당 인스턴스를 수정 → UPDATE
        
        ```jsx
        form = ArticleForm(request.POST)
        form.save()
        # create
        
        form = ArticleForm(request.POST, instance=article)
        form.save()
        # update
        ```
        
- update 페이지
    - instance는 수정 대상이 되는 기존 객체를 지정
    - request.POST
        - 사용자가 form을 통해 전송한 데이터 = 신규 데이터
    - instance
        - 신규 데이터를 받게 될 수정 대상
        - 코드 수정
        
        ```jsx
        # views.py
        def edit (request, pk)
        	article = Article.objects.get(pk=pk)
        	form = ArticleForm(instance=pk)
        	context = {'article':article, 'form':form}
        	return render(request, 'articles/edit.html', context)
        
        def update(request,pk):
        	article = Article.objects.get(pk=pk)
        	form = ArticleForm(requsest.POST, instance = article)
        	if form.is_valid():
        		form.save()
        		return redirect('articles:detail',article.pk)
        	context = {'form':form, 'article':article,}
        	return render(request, 'articles/edit.html', context)
        	
        # edit.html
        ...
        {% csrf token %}
        {{form.as_p}}
        ...
        ```
        
- form 과 modelform의 차이점
- form
    - 사용자로부터 받는 데이터가 DB와 연관되어 있지 않을 때
    - 단순 데이터만 사용되는 경우
        - 로그인 등, 인증 과정에만 활용되고 DB에 저장되지 않음
        - DB저장은 회원가입이지.
- modelform
    - 사용자로부터 받는 데이터가 DB와 연관되어 있는 경우
    - 데이터의 유효성 검사가 끝나면 데이터를 어떤 레코드에 맵핑해야 할지 알고 있으므로 save() 호출이 바로 가능

### Widgets 활용

- 위젯을 작성하는 2가지 방법
- class 메타 안에 widgets 함수를 생성하거나 (비추천)
- Form 안에 widget을 작성 (추천)

```jsx
class ArticleForm(forms.ModelForm):
	title = forms.Charfield(
		label = '제목',
		widget=forms.TextInput(
			attrs={
				'class':'my-title',
				'placeholder':'Enter the title',
				'maxlength':10,
			}
		)
	)
	
	content = forms.Charfield(
		label='내용',
		widget = forms.Textarea(
			attrs={
			'class':'my-title',
			'placeholder':'Enter the title',
			'rows':5,
			'cols':	50,	
			}
		),
		error_message={
			'required':'Please enter your content'
		}
	)			

	class Meta:
		model=Article
		fields='__all__'
```

## Handling HTTP requests

- http requests 처리에 따른 view 함수의 구조 변화
- 데이터의 생성 (new-update)과 수정(edit-update)의 공통점과 차이점
    - 각각 생성과 수정을 위한 로직
    - new와 edit은 get 요청에 대한 처리 (페이지 렌더링)
    - create와 update는 post 요청에 대한 처리만을 진행 (데이터 생성과 수정)
- 이를 기반으로, 하나의 view함수에서 로직을 분리

### CREATE

- new와 create 함수를 합침
    
    ```jsx
    def create(request):
    	if request.method=='POST':
    		form = ArticleForm(request.POST)
    		if form.is_valid():
    			article = form.save()
    			return redirect('articles:detail'. article.pk)
    	else:
    		form = ArticleForm()
    	context = {'form':form,}
    	return render(request, 'articles/create.html',context)
    ```
    
    - new의 view함수와 url_path를 삭제.
    - new.html의 이름을 create.html로 변경
    - html 내 action 속성 값 변경 `action="{%'url 'articles:create'%}"`
    - views 함수의 템플릿 경로 수정
    - index 페이지 내 new 링크 수정

### UPDATE

- edit과 update 함수를 합침
    
    ```jsx
    def update(request, pk):
    	article=Article.objects.get(pk=pk)
    	if request.method=='POST':
    		form=ArticleForm(request.POST, instance=article)
    		if form.is_valid():
    			form.save()
    			return redirect('articles:detail',article.pk)
    	else:
    		form=ArticleForm(instance=article)
    	context={'form': form, 'article': article,}
    	return render(request, 'articles/update.html', context)
    ```
    
    - edit의 view함수와 url_path를 삭제.
    - edit.html의 이름을 update.html로 변경
    - html 내 action 속성 값 변경 `action="{%'url 'articles:update'%}"`
    - views 함수의 템플릿 경로 수정
    - index 페이지 내 edit 링크 수정
    - POST 요청에 대해서만 삭제가 가능하도록 수정
        
        ```jsx
        def delete(request, pk):
        	article = Article.objects.get(pk=pk)
        	if request.method =='POST'
        		article.delete()
        		return redirect('articles:index')
        	return redirect('articles:detail', article.pk)
        ```
        

## View decorators

### 데코레이터

- 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수
- Django는 다양한 http 기능을 지원하기 위해 view함수에 적용할 수 있는 데코레이터를 제공

```jsx
def hello(func):
	def wrapper():
		print('HIHI')
		func()
		print('HIHI')
	retrun wrapper
# 함수

@hello
def bye():
	print('byebye')
# 데코레이터 부분
```

### Allowed HTTP methods

- 요청 메서드를 기반으로 접근을 제한
- 일치하지 않는 메서드 요청이라면 405 Method Not Allowed를 반환
- 목록
    - require_http_methods()
    - require_POST()
    - require_safe()

```jsx
# views.py

from django.views.decorators.http import require_http_methods, require_POST
@require_http_methods(['GET','POST'])
def create(request):
	....

@require_http_methods(['GET','POST'])
def update(request):
	....

@require_POST
def delete(request, pk):
	....

# 각각 해당하는 함수 윗부분에 데코레이터를 추가
# GET 또는 POST 일 경우에만 작업 (뒤에 원하는 method들의 리스트 추가)
# POST 일때만 작업 (해당 method가 뒤에 붙음)
# GET으로 받고 싶은 경우 require_GET보다는 require_safe를 사용
```