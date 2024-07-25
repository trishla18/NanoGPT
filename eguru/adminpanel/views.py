from django.shortcuts import render
from login.models import Users
from .models import Faculty

# Create your views here.
def adminPage(request):
    return render(request,"admin.html")

def getUsers(request):
    users = Users.objects.all()
    user_list = list(users.values())
    return JsonResponse(user_list, safe=False)

def addUser(request):
    new_user = Users(email=request.POST["email"], name=request.POST["name"], password=request.POST["password"])
    new_user.save()

def deleteUser(request):
    user = get_object_or_404(Users, email=request.POST["email"])
    user.delete()

def getFaculty(request):
    faculty = Faculty.objects.all()
    faculty_list = list(faculty.values())
    return JsonResponse(faculty_list, safe=False)

def addFaculty(request):
    new_faculty = Faculty(email=request.POST["femail"], name=request.POST["name"], designation=request.POST["designation"], topic_id=request.POST["topic"])
    new_faculty.save()

def deleteFaculty(request):
    faculty = get_object_or_404(Faculty, email=request.POST["femail"])
    faculty.delete()
