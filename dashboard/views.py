from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request, "index.html")

