from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'mainmenu/index.html')

def about_games(request):
    return render(request, 'mainmenu/about_games.html')

def about_programming(request):
    return render(request, 'mainmenu/about_programming.html')

def my_work(request):
    return render(request, 'mainmenu/my_work.html')

def PC(request):
    return render(request, 'mainmenu/Games/PC.html')

def Android(request):
    return render(request, 'mainmenu/Games/Android.html')

def PlayStation(request):
    return render(request, 'mainmenu/Games/PlayStation.html')

def IOS(request):
    return render(request, 'mainmenu/Games/IOS.html')