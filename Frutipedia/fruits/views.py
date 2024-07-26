from django.shortcuts import render

from Frutipedia.fruits.models import Fruit


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {
        'fruits': fruits
    }
    return render(request, 'common/dashboard.html', context)


def create_categories(request):
    return render(request, 'categories/create-category.html')


def create_fruit(request):
    return render(request, 'fruits/create-fruit.html')


def delete_fruit(request, pk):
    return render(request, 'fruits/delete-fruit.html')


def detail_fruit(request, pk):
    return render(request, 'fruits/details-fruit.html')


def edit_fruit(request, pk):
    return render(request, 'fruits/edit-fruit.html')


