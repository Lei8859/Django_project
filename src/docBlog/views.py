from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def test(resquest):
    return HttpResponse("<h1>TEST</h1>")
