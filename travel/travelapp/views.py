from django.http import HttpResponse
from django.shortcuts import render
from . models import place,team

# Create your views here.



def demo(request):
    obj=place.objects.all()
    obj2=team.objects.all()
    return render(request,'index.html',{'imgx':obj,'imgy':obj2})























# def addition(request):
#     x=int(request.GET['Number1'])
#     y=int(request.GET['Number2'])
#     result=x+y
#     return render(request,"pvalue.html",{'ans':result})

# def about(request):
#     return render(request,'frontpage.html')
#
# def contact(request):
#     return HttpResponse('This is a contact page')
