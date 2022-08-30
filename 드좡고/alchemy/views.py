from django.shortcuts import render

# Create your views here.
def index(request):
    pass
    return render(request, 'alchemy/index.html')

def clap(request):
    pass
    return render(request, 'alchemy/clap.html')

def throw(request) : 
    pass
    return render(request, 'alchemy/throw.html')

def catch(request) : 
    name = request.GET.get('message')
    context = {
        'name' : name,
    }
    return render(request, 'alchemy/catch.html',context)