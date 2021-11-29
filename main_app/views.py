from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
# ----- Authentication -----
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# ----- Authorization ----
from django.contrib.auth.decorators import login_required   # for view functions
from django.contrib.auth.mixins import LoginRequiredMixin   # for CBVs
# ----- Models & Forms-----
from .models import Classroom, Item
from .forms import ClassroomForm, ItemForm



# ========== GENERAL Views ==========
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# ========== AUTHENTICATION Views ==========
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()      # save user to database
            login(request, user)    # log user in
            return redirect('classroom_index')  # redirect to classroom_index page  # todo - is this where we want a newly signed up user to be redirected to?
        else:
            error_message = 'Invalid sign up - please try again.'
    form = UserCreationForm()       # reset the sign-up to a blank form if bad POST or GET request
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


# ========== CLASSROOM Views ==========
# ----- Index -----
class ClassroomIndex(LoginRequiredMixin, ListView):
    model = Classroom
    template_name = 'classroom_list.html'
    
    def get_queryset(self):
        queryset = Classroom.objects.filter(user=self.request.user)
        return queryset

# ----- Detail/Show as a view function -----
# @login_required
# def classroom_detail(request, classroom_id):
#     classroom = Classroom.objects.get(id=classroom_id)
#     # --- Instance Methods ---
#     return render(request, 'main_app/classroom_detail.html', {'classroom': classroom})

# ----- Detail/Show as a CBV -----
class ClassroomDetail(LoginRequiredMixin, DetailView):
    model = Classroom
    form_class = ItemForm
    # --- Instance Method returns context object data for display ---
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs, item_form = ItemForm())
        
        return context

# ----- Create -----
class ClassroomCreate(LoginRequiredMixin, CreateView):
    model = Classroom 
    form_class = ClassroomForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# ----- Update -----
class ClassroomUpdate(LoginRequiredMixin, UpdateView):
    model = Classroom
    form_class = ClassroomForm

# ----- Delete -----
class ClassroomDelete(LoginRequiredMixin, DeleteView):
    model = Classroom
    success_url = '/classrooms/'


# ========== WISHLIST Views (i.e., - associate item with classroom) ==========


# ========== ITEM Views ==========

def add_item(request, classroom_id):
    form = ItemForm(request.POST)
    if form.is_valid():
        new_item = form.save(commit=False)
        new_item.classroom_id = classroom_id
        new_item.save()
    else:
        result = form.is_valid()
        # print(result.errors)
    return redirect('classroom_detail', pk = classroom_id)

class ItemDetail(LoginRequiredMixin, DetailView):
    model = Item
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classroom'] = Classroom.objects.all()
        return context

class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/classrooms/' # add classroom.id to take them back to specific classroom

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = '__all__'
    success_url = '/classrooms/' # add classroom.id to take them back to specific classroom