from django.urls import path

from .views import index_ecoshop, info_ecoshop, products_ecoshop, comments_ecoshop, products_catalog

urlpatterns = [
    path("index/", index_ecoshop, name="index_ecoshop"),
    path("info/<int:address>/", info_ecoshop, name="info_ecoshop"),
    path("products/", products_ecoshop, name="products_ecoshop"),
    path("comments/", comments_ecoshop, name="comments_ecoshop"),
    path("products_catalog/", products_catalog),
]
