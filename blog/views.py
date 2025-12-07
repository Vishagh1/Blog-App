from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         "author":"vishagh",
#         "title":"Title1",
#         "content":"Good",
#         "date_posted":"23-5-25"
#     },
#     {
#         "author":"visal",
#         "title":"Title2",
#         "content":"BAD",
#         "date_posted":"29-5-25"
#     }
# ]

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,"blog/home.html",context)

def about(request):
    context = {
        "title":"vishagh's blog"
    }
    return render(request, "blog/about.html",context)
# Create your views here.