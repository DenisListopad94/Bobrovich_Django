from django.contrib import admin
from django.urls import path, include
from .views import VendorsList, VendorDetail, ShippersList, ShipperDetail

urlpatterns = [
    path('vendors/', VendorsList.as_view()),
    path('shippers/', ShippersList.as_view()),
    path('vendor/<int:pk>/', VendorDetail.as_view()),
    path('shipper/<int:pk>/', ShipperDetail.as_view())
]
