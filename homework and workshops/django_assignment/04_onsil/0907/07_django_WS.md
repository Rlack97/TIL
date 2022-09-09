1. 유저 목록 출력
def user_list(request):
    user = User.objects.all()
    context = {
        'users': user,
    }
    return render(request, 'accounts/user_list.html', context)

[!1](1.png)

1. 회원가입 작성
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 후 로그인
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


[!2](2.png)
