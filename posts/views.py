from django.shortcuts import render
from django.http import HttpResponse

def wellcome(request):
    return HttpResponse("<h1>Wellcome to my web<h1>")
