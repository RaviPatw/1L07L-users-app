from django.shortcuts import render
from .models import User
# from django.http import HttpResponse

# Create your views here.
def register(request):
    users = User.objects.all()
    context = {
        'active_link': 'users',
        'users':users
    }
    return render(request,'users/register.html',context)