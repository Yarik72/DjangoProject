from django.shortcuts import render
from .UserRegister import UserForm
from .models import *


def get_platform(request):
    if request.method:
        return render(request, 'platform.html')


# Create your views here.

def get_games(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'games.html', context)


def get_cart(request):
    return render(request, 'cart.html')


def sign_up_by_django(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password == repeat_password and age >= 18 and username not in [user.name for user in users]:
                Buyer.objects.create(name=username, age=age)
                info['message'] = f"Приветствуем, {username}"
                form = UserForm()
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in [user.name for user in users]:
                info['error'] = 'Пользователь уже существует'
        info['form'] = form
    else:
        form = UserForm()
    info['form'] = form
    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    users = Buyer.objects.all()
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')


        info['username'] = username
        info['password'] = password
        info['repeat_password'] = repeat_password
        info['age'] = age
        if password == repeat_password and int(age) >= 18 and username not in [user.name for user in users]:
            Buyer.objects.create(name=username, age=age)
            info['message'] = f"Приветствуем, {username}"
            info['username'] = ''
            info['password'] = ''
            info['repeat_password'] = ''
            info['age'] = ''
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in [user.name for user in users]:
            info['error'] = 'Пользователь уже существует'

    return render(request, 'registration_page.html', info)

