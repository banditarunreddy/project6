from django.shortcuts import render

def jinja_second(request):

    d={'name':'tarun','age':'21'}

    return render(request,'jinja_second.html',context=d)
