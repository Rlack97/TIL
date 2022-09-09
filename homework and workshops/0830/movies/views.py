from django.shortcuts import render

# Create your views here.
def home(request):
    movie = ['Man from earth' ,'your name is' , 'child of weather']

    context = {
        'movie' : movie, 
    }
    return render(request, 'movies/home.html', context)