from http.client import HTTPResponse


from django.http import HttpResponse
from django.shortcuts import render

data = {
    "movies":[
        {
            'id':5,
            'title':'Om Shanti Om',
            'year':2013
        },
        {
            'id':6,
            'title':'Dabang',
            'year':2015
        },
        {
            'id':7,
            'title':'Bhulbhuliya',
            'year':2022
        },
    ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("This is a home page")