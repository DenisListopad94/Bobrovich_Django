from django.urls import path

from .views import index_ecoshop, info_ecoshop, products_ecoshop, comments_ecoshop, products_catalog, \
    vendors_info_ecoshop, shippers_info_ecoshop, create_product_ecoshop, create_shipperreviews_ecoshop, \
    create_vendorreviews_ecoshop

urlpatterns = [
    path("index/", index_ecoshop, name="index_ecoshop"),
    path("info/<int:address>/", info_ecoshop, name="info_ecoshop"),
    path("products/", products_ecoshop, name="products_ecoshop"),
    path("comments/", comments_ecoshop, name="comments_ecoshop"),
    path("products_catalog/", products_catalog),
    path("vendors_info/", vendors_info_ecoshop, name="vendors_info_ecoshop"),
    path("shippers_info/", shippers_info_ecoshop, name="shippers_info_ecoshop"),
    path("create_product/", create_product_ecoshop, name="create_product_ecoshop"),
    path("create_shipperreviews/", create_shipperreviews_ecoshop, name="create_shipperreviews_ecoshop"),
    path("create_vendorreviews/", create_vendorreviews_ecoshop, name="create_vendorreviews_ecoshop")
]
