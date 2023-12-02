from django.shortcuts import render

# Create your views here.


def home(request):
    d = {"name": "django", "list": ["rakib", "sakib", "akib", "nakib"]}
    return render(request, "home.html", d)


def context(request):
    d = {
        "letters": ["a", "b", "c", "d"],
        "num": 22,
        "quotes": "Hello",
        "greetings": "Its computer",
        "name": "superman",
        "status": "",
        "guys": [
            {"name": "sil", "age": 19},
            {"name": "fil", "age": 22},
            {"name": "gil", "age": 31},
        ],
        "file": 123456789,
    }
    return render(request, "context.html", d)