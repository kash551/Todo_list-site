from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
 
# import todo form and models
 
from .forms import TodoForm
from .models import Todo
from .forms import UserProfileForm
from .models import UserProfile
###############################################
 
def index(request):
 
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo/index.html')
    form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "Home",
    }
    return render(request, 'todo/index.html', page)
 
 
### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')

def checklist(request):
    return render(request, 'todo/checklist.html')