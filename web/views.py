from django.shortcuts import render


def index(request):
    return render(request, 'web/index.html')


def item(request, id):
    return render(request, 'web/item.html')
