from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movie_list' : [
        {
            'id' : 5,
            'title' : 'Jaws',
            'year' : 1969,
        },
        
        {
            'id' : 6,
            'title' : 'Sharknado',
            'year' : 1980,
        },
        
        {
            'id' : 7,
            'title' : 'The meg',
            'year' : 1940,
        
        },
        
    ]
}

def movies(request):
    return render(request, 'movies/movie_list.html', data)


def home(request):
    return HttpResponse("homepage")