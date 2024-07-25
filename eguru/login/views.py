from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Users

# Create your views here.
def loginPage(request):
    return render(request, "index.html")

@csrf_exempt
def login(request):
    try:
        user = Users.objects.get(email=request.POST["email"], password=request.POST["password"])
    except Users.DoesNotExist:
        user = None
    if user is None:
        return JsonResponse({"flag": "0", "name": ""})
    return JsonResponse({"flag": "1", "name": user.name})