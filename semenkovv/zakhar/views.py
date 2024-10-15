
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "homee.html")
def name(request):
    return HttpResponse("Имя: Захар, Фамилия: Семенков")

def groupe(request):
    return HttpResponse("Группа: БИН-22-2")

def age(request):
    return HttpResponse("Возраст: 20")

def common(request):
    return HttpResponse("Имя: Захар, Фамилия: Семенков, Группа: БИН-22-2, Возраст: 20")
# Create your views here.

# Create your views here.
