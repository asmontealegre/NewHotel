from django.views.defaults import page_not_found
from django.shortcuts import render



def Home(request):
    return render(request,"index.html")

def error_404(request,exception):
    return page_not_found(request,'404.html')

