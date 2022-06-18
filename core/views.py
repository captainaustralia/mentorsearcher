from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

from core.models import Technologies, Request


def index(request):
    return render(request, 'index.html')


# @login_required ЕСЛИ ХОТИТЕ ЧТОБЫ ВЫ МОГЛИ ПОЛЬЗОВАТЬСЯ ЭТИМИ ФУНКИЦЯМИ ТОЛЬКО ЗАЛОГИНЕНЫМ ПОЛЬЗОВАТЕЛЯМ РАСКОМЕНТИТЕ ЭТО
def create_tech(request):
    if request.method == 'GET':
        return render(request, 'create_tech.html')
    if request.method == 'POST':
        new_tech = Technologies()
        new_tech.title = request.POST['title']
        new_tech.save()
        return render(request, 'success.html')


# @login_required ЕСЛИ ХОТИТЕ ЧТОБЫ ВЫ МОГЛИ ПОЛЬЗОВАТЬСЯ ЭТИМИ ФУНКИЦЯМИ ТОЛЬКО ЗАЛОГИНЕНЫМ ПОЛЬЗОВАТЕЛЯМ РАСКОМЕНТИТЕ ЭТО
def create_request(request):
    if request.method == 'GET':
        technologies = Technologies.objects.all()
        context = {'tech': technologies}
        return render(request, 'create_request.html', context)
    if request.method == 'POST':
        new_request = Request()
        new_request.title = request.POST['title']
        new_request.tech = Technologies.objects.get(title=request.POST['tech'])
        if request.POST["search_mentor"] == 'on':
            new_request.search_mentor = True
        else:
            new_request.search_mentor = False
        new_request.creator = User.objects.get(id=request.user.id)
        new_request.save()
        return render(request, 'success.html')

# Если вам нужно добавить в модель ManyToManyField объекты,
# вы делаете это через метод .add(Внутрь передаете queryset с нужными объектами)
# ЕСЛИ ЗАТУПИЛИ ГУГЛИТЕ HOW ADD MANY TO MANY OBJECTS
# ПЕРЕД ТЕМ КАК ДОБАВЛЯТЬ КАКИЕ ТО ОБЪЕКТЫ В FK , M2M ВЫ ДОЛЖНЫ ЭТИ ОБЬЕКТЫ СОЗДАТЬ!

# LISTVIEW , DETAILVIEW, CREATEVIEW
