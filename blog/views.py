from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from django.utils import timezone

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image']:
            blog = Blog()
            blog.title = request.POST['title']
            blog.body = request.POST['body']
            blog.image = request.FILES['image']
            blog.pub_date = timezone.datetime.now()
            blog.hunter = request.user
            blog.save()
            return redirect('home')

        else:
            return render (request,'blog/create.html',{'error':'All fields are required'})


    else:
        return render(request,'blog/create.html')
