from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'posts/index.html',context)

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            print(request.FILES)
            if form.is_valid():
                post = form.save()
                return redirect('posts:index')
        else:
            form = PostForm()
            flag = False
        context={
            'form':form,
            'flag':flag,
        }
        return render(request,'posts/form.html', context)
    else:
        return redirect('accounts:login')
    

def update(request,pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)
        flag = True
        if request.method=="POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('posts:index')
        else:
            form = PostForm(instance=post)
        context = {
            'form':form,
            'post':post,
            'flag':flag
        }
        return render(request,'posts/form.html', context)
    else:
        return redirect('accounts:login')


def delete(request,pk):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('posts:index')
    else:
        return redirect('accounts:login')