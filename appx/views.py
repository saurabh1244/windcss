from django.shortcuts import render , HttpResponse , redirect
from .models import blogx ,comment
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


def register_page(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        passx = request.POST.get('passx')

        print(fname, lname, email,passx ,username )



        obj = User.objects.create(username = username , first_name=fname,last_name=lname,email=email )
        obj.set_password(passx)
        obj.save()

        print(fname, lname, email,passx ,username )

    return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        passx = request.POST['passx']

        if User.objects.filter(username=username).exists():
            user_obj = authenticate(username=username,password=passx)
            login(request,user_obj)
            print('login sucess using ...')
            print(username,passx)
            return redirect('/')

        else:
            return HttpResponse('any error occuredin if statement')

    return render(request , 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/')

def page(request):
    obj = blogx.objects.all()
    context = {
        'datas': obj
    }
    return render(request , 'index.html',context)
    

def home(request):
       return render(request, 'home.html')



def post(request,slug):
    cum_obj = None
    if request.method == 'POST':
        commentx = request.POST['comment']
        print(comment)

        obj = blogx.objects.get(slugx=slug)

        cum_obj = comment.objects.create(cum_id=obj,text=commentx)
        cum_obj.save()
        print("succefully added comments...")



    obj = blogx.objects.get(slugx=slug)
    comments = comment.objects.filter(cum_id=obj).order_by('-id')

    context = {
        'html':obj,
        'new_comment':cum_obj,
        'comments':comments
    }

    return render(request , 'datax.html',context)

@login_required(login_url='/login/')
def post_user(request):
    if request.method == 'POST':
        blog_id = request.POST['blog_id']
        blog_name = request.POST['blog_name']
        blog_code = request.POST['blog_code']
        blog_desc = request.POST['blog_desc']

        obj = blogx.objects.create(blog_id=blog_id, blog_name=blog_name, blog_code=blog_code, blog_desc=blog_desc)
        obj.save()
        return HttpResponse('add blog succesfully..')


    return render(request , 'post_user.html')