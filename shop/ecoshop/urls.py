from django.urls import path

from .views import index_ecoshop, info_ecoshop

urlpatterns = [
    path("index/", index_ecoshop),
    path("info/<int:address>/", info_ecoshop),
]