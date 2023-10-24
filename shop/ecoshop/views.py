from django.shortcuts import render
from django.http import HttpResponse


def index_ecoshop(request):
    return HttpResponse("Hello, world. You're at the ecoshop index.")


def info_ecoshop(request, address):
    return HttpResponse(f"Ecoshop on address Prityckogo, {address}.")
