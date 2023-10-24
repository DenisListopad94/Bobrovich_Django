from django.urls import path

from .views import index_ecoshop, info_ecoshop, products_catalog

urlpatterns = [
    path("index/", index_ecoshop),
    path("info/<int:address>/", info_ecoshop),
    path("products_catalog/", products_catalog),
]
