from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request,*args, **kwargs):
    print(*args, **kwargs)
    print(request.user)
    # return HttpResponse("<h1>Welcome to mysite.<br>This is my first app implementation...</h1>")
    return render(request, "home.html",{"name":"nani","age":24})

def contact_view(request,*args, **kwargs):
    # return HttpResponse("<h1>Contact Page....</h1><br><br><h3>This page is underconstructing, so stay with me. We'll be back as soon as possible</h3>")
    my_context = {
        "name":"siva",
        "num":123
    }
    return render(request, "contact.html",my_context)

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text":"This is about us...",
        "my_num":312,
        "my_list":[123, 4242, 312, "Abc"],
        "this_is_true":True
    }
    # for item in [123, 12331, 1233]:
    #     my_context['item1']=item
    return render(request,"about.html",my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social Page</h1>")