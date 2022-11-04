from django.http import HttpResponse
from django.shortcuts import render
from.models import *


# Create your views here.
def index(requesst):
    blogsdata=blog.objects.all()
    context={"blogs":blogsdata}
    for i in blogsdata:
        print(i )
    return render(requesst, "index.html", context=context)
 
 