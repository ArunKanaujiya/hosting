from django.shortcuts import render,redirect
from WebApp.models import Customer,Book,Student
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def register(request):
    if request.method=='POST':
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already Taken..!')
            return redirect('/register')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Acount Created Succesfully...!')

        
        return redirect('/register')
    return render(request,'myapp/register.html')

def login_page(request):
    if request.method=='GET':
        return render(request,'myapp/login.html')
    
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'invalid username')
            return redirect('/login')
        
        else:
            return redirect('/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'invalid password')
            return redirect('/login/')
        else:
            login(request,user)

    return render(request,'myapp/login.html')

def logout_page(request):
    return render(request,'myapp/logout.html')

@login_required(login_url='/login')
def Cust_page(request):
    if request.method=='POST':
        data=request.POST
        image=request.FILES.get('image')
        name=data.get('name')
        age=data.get('age')
        address=data.get('address')
        Customer.objects.create(
            name=name,
            age=age,
            address=address,
            image=image

        )
        print(image)
        messages.error(request,'Customer name submitted succesfully')
        return redirect('/')
        
    return render(request,'myapp/customer.html',{'context':Cust_page})


def index(request):
    customer=Customer.objects.all()
    return render(request, "myapp/index.html",{'customer':customer})

@login_required(login_url='/login')
def Book_page(request):
    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        author=data.get('author')
        price=data.get('price')
        category=data.get('category')
        books=Book.objects.create(
            name=name,
            author=author,
            price=price,
            category=category
        )
        books.save()
    return render(request,'books/book.html',{'context':Book_page})

@login_required(login_url='/login')
def Book_show(request):
    data=Book.objects.all()
    return render(request,'books/bookshow.html',{'data':data})

@login_required(login_url='/login')
def student_page(request):
    if request.method=='GET':
        return render(request,'students/addstudent.html')
    else:
        request.method=='POST'
        data=request.POST
        image=request.FILES.get('image')
        classroom=data.get('classroom')
        branch=data.get('branch')
        roll_no=data.get('roll_no')
        phone=data.get('phone')
        students=Student.objects.create(
            classroom=classroom,
            branch=branch,
            roll_no=roll_no,
            phone=phone,
            image=image
        )
        students.save()
        print(image)
        messages.error(request,'Student Save Successfully..!')
        return redirect('/student')
    return redirect(request,'students/addstudent.html',{'context':Student})
    




