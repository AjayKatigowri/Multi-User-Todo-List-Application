from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Todo

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('todos')
        return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def todos_view(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos.html', {'todos': todos})

@require_POST
@login_required(login_url='login')
def add_todo(request):
    title = request.POST['title']
    Todo.objects.create(title=title, user=request.user, description='')
    return redirect('todos')

@require_POST
@login_required(login_url='login')
def toggle_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todos')

@require_POST
@login_required(login_url='login')
def delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('todos')