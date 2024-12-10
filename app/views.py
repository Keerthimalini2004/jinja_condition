from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'name':'malini','age':20,'marks':456,'grade':2,'a':15}
    return render(request,'condition.html',context=d)