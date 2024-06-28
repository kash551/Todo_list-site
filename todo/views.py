from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
 
# import todo form and models
 
from .forms import TodoForm
from .models import Todo
from .forms import UserProfileForm
from .models import UserProfile
###############################################
 
@login_required
def index(request):
 
    item_list = Todo.objects.filter(user=request.user).order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:index')
    form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "Home",
    }
    return render(request, 'todo/index.html', page)
 
 
### function to remove item, it receive todo item_id as primary key from url ##
@login_required
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo:index')
