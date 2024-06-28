from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import generic, View
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

    return render(request, 'todo/index.html') 

class Checklist(View):
    def get(self, request):
        items = Todo.objects.all()
        form = TodoForm()
        
        # Calculate remaining spoons for each item
        for item in items:
            user_profile = UserProfile.objects.get(user_id=item.user_profile.user_id)
            item.remaining_spoons = user_profile.max_spoons - item.spoons_required
        
        return render(request, "todo/checklist.html", {"items": items, "form": form})

    def post(self, request):
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            # Redirect to the same page to reflect the change
            return redirect('checklist', items=items, form=form)
        else:
            # If the form is not valid, re-render the form with errors
            return render(
                request,
                "todo/checklist.html",
                {
                    "form": form
                },
            )


### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')
