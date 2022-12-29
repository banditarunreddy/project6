from django.shortcuts import render

def jinja_first(request):
    
    d={'name':'tarun'}

    return render(request,'jinja_first.html',context=d)

