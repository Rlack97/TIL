from django.shortcuts import render, redirect
from chattings.forms import ChatForm
from chattings.models import Chat

# Create your views here.
def index(request):
    return render(request, 'chattings/index.html')

def create(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid:
            chat = form.save()
            return redirect( request, 'chattings:detail', chat.pk)
    else:
        form = ChatForm
    context = {
        'form':form
    }
    return render(request, 'chattings/create.html', context)


def detail(request, pk):
    chat = Chat.objects.get(pk=pk)
    context = {'chat':chat}
    return render(request, 'chattings/detail.html', context)