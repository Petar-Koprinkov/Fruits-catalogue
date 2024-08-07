from django.shortcuts import render, redirect

from Frutipedia.fruits.forms import CreateCategory, CreateFruits, EditFruits, DeleteFruits
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
    if request.method == 'GET':
        form = CreateCategory()
    else:
        form = CreateCategory(request.POST)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'categories/create-category.html', context)


def create_fruit(request):
    if request.method == 'GET':
        form = CreateFruits()
    else:
        form = CreateFruits(request.POST)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'fruits/create-fruit.html', context)


def detail_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)

    context = {
        'fruit': fruit
    }
    return render(request, 'fruits/details-fruit.html', context)


def edit_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditFruits(instance=fruit)
    else:
        form = EditFruits(request.POST, instance=fruit)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }
    return render(request, 'fruits/edit-fruit.html', context)


def delete_fruit(request, pk):
    fruit = Fruit.objects.get(pk=pk)
    if request.method == 'GET':
        form = DeleteFruits(instance=fruit)
    else:
        form = DeleteFruits(request.POST, instance=fruit)

    if form.is_valid():
        fruit.delete()
        return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }

    return render(request, 'fruits/delete-fruit.html', context)

