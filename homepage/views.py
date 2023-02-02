from django.shortcuts import render

# Create your views here.

def IndexView(request):
    #return(HttpResponse("Index view"))
    return render(request,'homepagetemplates/homepage.html',context={})
