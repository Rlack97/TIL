from django.shortcuts import render

# Create your views here.
def id(request):
    pass
    return render( request, 'submits/id.html')

def password(request):
    A = request.GET.get('id')
    context = {'A':A}
    return render( request, 'submits/password.html', context)