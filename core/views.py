from django.shortcuts import render,redirect
from .models import Todo
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import get_object_or_404
from .forms import EditTodo
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        id = request.user.id
        all_todos = Todo.objects.all().filter(user=id).order_by('-created_at')
        if all_todos is not None:
            return render(request,'index.html',{'all_todos':all_todos})
        else:
            return render(request,'index.html',{'all_todos':None})
    return render(request,'index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            exist_user = User.objects.filter(username=username)
            if exist_user:
                messages.warning(request,'This username is already exist')
                return redirect('register')
            else:
                new_user = User.objects.create(username=username)
                new_user.set_password(password)
                new_user.save()
                login(request,new_user)
                return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')

    return render(request,'register.html',{'form':form})

def log_in(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request,'Invalid Credentials')
                return redirect('login')
    return render(request,'login.html',{'form':form})

def log_out(request):
    logout(request)
    return redirect('/')

@csrf_exempt
def add_todo(request):
    if request.method == 'POST':
            if request.user.is_authenticated:
                data = json.loads(request.body)['data']
                print(data)
                print(request.user)
                new_todo = Todo(user=request.user,content=data)
                new_todo.save()
                return JsonResponse({'message': 'Data received successfully','status':'success'})
            else:
                return JsonResponse({'message': 'You are authrozied','status':'warning'})
            
@login_required
def delete_todo(request,pk):
    print(pk)
    todo = get_object_or_404(Todo,pk=pk)
    todo.delete()
    return redirect('index')

@login_required
def edit_todo(request,pk):
    form = EditTodo(request.POST or None)
    if request.method == 'POST':
        todo = get_object_or_404(Todo,pk=pk)
        if request.user != todo.user:
            return render(request,'forbidden.html')
        else:
            data = request.POST.get('content')
            todo.content = data
            todo.save()
            return redirect('index')
    return render(request,'edit.html',{'form':form})
