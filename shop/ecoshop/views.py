from django.shortcuts import render
from .models import ProductReviews, Vendor, Shipper
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
    comments = ProductReviews.objects.select_related("product").all

    context = {
        "comments": comments
    }
    return render(request, "comments.html", context=context)


def products_catalog(request):

    context = {
        "products": PRODUCTS
    }

    return render(request, "products_catalog.html", context=context)


def vendors_info_ecoshop(request):
    vendors = Vendor.objects.prefetch_related("product").all#prefetch_related("vendor__vendorreviews_set").

    context = {
        "vendors": vendors
    }

    return render(request, "vendors_info.html", context=context)


def shippers_info_ecoshop(request):
    shippers = Shipper.objects.prefetch_related("product").all#prefetch_related("shipper__shipperreviews_set").

    context = {
        "shippers": shippers
    }

    return render(request, "shippers_info.html", context=context)