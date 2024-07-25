from django.shortcuts import render

# Create your views here.
def subjectsPage(request):
    return render(request, "subjects.html")