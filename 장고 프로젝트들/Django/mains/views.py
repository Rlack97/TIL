from django.shortcuts import render

# Create your views here.
def startpage(request):
    A = 'Melty Blood Type:Lumina'
    context = {'title' : A}
    return render(request, 'mains/startpage.html', context)