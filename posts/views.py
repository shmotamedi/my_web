import json

from django.shortcuts import render
from django.http import HttpResponse

def wellcome(request):
    text1="<h1>Wellcome to my web<h1>"
    text2="<h2>Wellcome to my web<h2>"
    text3="<h3>Wellcome to my web<h3>"
    note=[text3,text2,text1]
    note="\n".join(note)
    return HttpResponse(note)