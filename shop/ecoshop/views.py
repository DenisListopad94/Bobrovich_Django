from django.shortcuts import render
from django.http import HttpResponse

PRODUCTS = {
    "apple": {
        "cost": 4.24,
        "count": 1000,
        "delive": ["Belarus", "Poland", "Russia"]
    },
    "orange": {
        "cost": 7.24,
        "count": 100,
        "delive": ["SAR", "Spain", "Portugal"]
    },
    "grape": {
        "cost": 11.33,
        "count": 1000,
        "delive": ["Spain", "Turkey", "Italy"]
    }
}


def index_ecoshop(request):
    return render(request, "index.html")


def info_ecoshop(request, address):

    context = {
        "address": address
    }

    return render(request, "info.html", context=context)


def products_ecoshop(request):
    return render(request, "products.html")


def comments_ecoshop(request):
    return render(request, "comments.html")


def products_catalog(request):

    context = {
        "products": PRODUCTS
    }

    return render(request, "products_catalog.html", context=context)
