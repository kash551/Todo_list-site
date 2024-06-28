from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import generic,View
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


# def checklist(request):

#     form = TodoForm()
#     print(form)
#     return render(request, "todo/checklist.html", {"form": form})
 

class Checklist(View):

    def get(self, request):
        items = Todo.objects.all()
        form = TodoForm()
        return render(request, "todo/checklist.html",{"items": items,"form": form})


    def post(self, request):
        """What happens for a POST request"""
        form = TodoForm(request.POST)

        if form.is_valid():
            form = form.save()
            form.save()
            return redirect('todo/checklist.html')
        else:
            form = TodoForm()

        return render(
            request,
            "todo/checklist.html",
            {
                "form": form

            },
        )

    # template_name = "templates/todo/checklist.html" 
    
    # def postdetails(self):
    #     return ToDo.objects

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = TodoForm()
    #     return context

    #     item_list = Todo.objects.order_by("-date")

    #     if request.method == "POST":
    #         form = TodoForm(request.POST)
    #         if form.is_valid():
    #                 form.save()
    #                 return redirect('todo/index.html')
    #         else:
    #             form = TodoForm()
    
    #     page = {
    #             "form": form,
    #         "list": item_list,
    #         "title": "Home",
    #     }
    #     return render(request, 'todo/checklist.html', page)
    
 
### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')
