from django.shortcuts import render

# Create your views here.
def topicsPage(request):
    return render(request, "topics.html")