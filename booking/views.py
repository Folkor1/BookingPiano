from django.shortcuts import render

def homepage(request):
    """
    Render the home page.
    """
    return render(request, "index.html")

def about(request):
    """
    Render about page.
    """
    return render(request, "about.html")

