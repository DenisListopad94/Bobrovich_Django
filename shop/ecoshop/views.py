from django.core.paginator import Paginator
from django.shortcuts import render
from .models import ProductReviews, Vendor, Shipper, Product
from .forms import ProductForm, ShipperReviewsForm, VendorReviewsForm
from django.http import HttpResponseRedirect

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
    products = Product.objects.all()
    paginator = Paginator(products, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "products.html", {"page_obj": page_obj})


def comments_ecoshop(request):
    comments = ProductReviews.objects.select_related("product").all()

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
    vendors = Vendor.objects.prefetch_related("product").all()#prefetch_related("vendor__vendorreviews_set").

    context = {
        "vendors": vendors
    }

    return render(request, "vendors_info.html", context=context)


def shippers_info_ecoshop(request):
    shippers = Shipper.objects.prefetch_related("product").all()#prefetch_related("shipper__shipperreviews_set").

    context = {
        "shippers": shippers
    }

    return render(request, "shippers_info.html", context=context)


def create_product_ecoshop(request):

    context = {}

    if request.method == "POST":

        form = ProductForm(request.POST)
        form.save()

        if form.is_valid():
            # product = ProductForm(**form.cleaned_data)
            # product.save()
            return HttpResponseRedirect("/ecoshop/products/")
    else:
        form = ProductForm()

    context["form"] = form
    return render(request, "create_product.html", context=context)


def create_shipperreviews_ecoshop(request):

    context = {}

    if request.method == "POST":

        form = ShipperReviewsForm(request.POST)
        form.save()

        if form.is_valid():
            return HttpResponseRedirect("/ecoshop/shippers_info/")
    else:
        form = ShipperReviewsForm()

    context["form"] = form
    return render(request, "create_shipperreviews.html", context=context)


def create_vendorreviews_ecoshop(request):

    context = {}

    if request.method == "POST":

        form = VendorReviewsForm(request.POST)
        form.save()

        if form.is_valid():
            return HttpResponseRedirect("/ecoshop/vendors_info/")
    else:
        form = VendorReviewsForm()

    context["form"] = form
    return render(request, "create_vendorreviews.html", context=context)
