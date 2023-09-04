import logging
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import forms
from . import models

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = forms.UserForm()
    return render(request, 'app4/user_form.html', {'form': form})


def many_fields_form(request):
    if request.method == 'POST':
        form = forms.ManyFieldsFormWidget(request.POST)
        if form.is_valid():
            # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = forms.ManyFieldsFormWidget()
    return render(request, 'app4/many_fields_form.html', {'form': form})


def add_user(request):
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            logger.info(f'Получили {name=}, {email=}, {age=}.')
            user = models.User(name=name, email=email, age=age)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = forms.UserForm()
        message = 'Заполните форму'
    return render(request, 'app4/user_form.html', {'form': form, 'message': message})


def upload_image(request):
    if request.method == 'POST':
        form = forms.ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = forms.ImageForm()
    return render(request, 'app4/upload_image.html', {'form': form})
