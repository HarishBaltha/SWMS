from django.shortcuts import render

def sing(request):
    return render(request,"sing.html")

def click(request):
    return render(request, "click.html")

def company(request):
    return render(request,"company.html")

def awards(request):
    return render(request, "awards.html")

def awards1(request):
    return render(request, "awards1.html")

def awards2(request):
    return render(request, "awards2.html")

def awards3(reqest):
    return render(reqest, "awards3.html")

def awards4(request):
    return render(request, "awards4.html")

def line(request):
    return render(request, "line.html")