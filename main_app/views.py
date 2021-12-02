from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# ----- Authentication -----
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# ----- Authorization ----
from django.contrib.auth.decorators import login_required   # for view functions
from django.contrib.auth.mixins import LoginRequiredMixin   # for CBVs
# ----- Models & Forms-----
from django.db.models import Q
from .models import Classroom, Item
from .forms import ClassroomForm, ItemForm


# ========================================
#          GENERAL Views
# ========================================
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# ========================================
#          AUTHENTICATION Views
# ========================================
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()      # save user to database
            login(request, user)    # log user in
            return redirect('classroom_list')  
        else:
            error_message = 'Invalid sign up - please try again.'
    form = UserCreationForm()       # reset the sign-up to a blank form if bad POST or GET request
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


# ========================================
#          CLASSROOM Views
# ========================================
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
class ClassroomDetail(DetailView):
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


# ========================================
#          ITEM Views
# ========================================
# ----- Create -----
def add_item(request, classroom_id):
    form = ItemForm(request.POST)
    if form.is_valid():
        new_item = form.save(commit=False)
        new_item.classroom_id = classroom_id
        new_item.save()
    else:
        result = form.is_valid()
        print(result.errors)
    return redirect('classroom_detail', pk = classroom_id)

# ----- Detail/Show -----
class ItemDetail(DetailView):
    model = Item
    
    def get_context_data(self, **kwargs):
        context = super(ItemDetail, self).get_context_data(**kwargs)
        classroom = self.object.classroom
        context['classroom'] = classroom
        return context
        
# ----- Update -----
class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name', 'amount', 'thumbnail', 'notes']
   
# ----- Delete -----
class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item

    def get_success_url(self):
        classroom = self.object.classroom
        return reverse('classroom_detail', kwargs={'pk':classroom.id})


# ========================================
#          SEARCH Views
# ========================================
class SearchResultsView(ListView):
    model = Classroom
    template_name = 'search_results.html'

    def get_queryset(self):
        if (self.request.GET.get('school_name') != None):
            query = self.request.GET.get('school_name')
            object_list = Classroom.objects.filter(Q(school_name__icontains=query))
        if (self.request.GET.get('state') != None):
            query = self.request.GET.get('state')
            object_list = Classroom.objects.filter(Q(state__icontains=query))
        if(self.request.GET.get('district') != None):
            query = self.request.GET.get('district')
            object_list = Classroom.objects.filter(Q(district__icontains=query))
        if(self.request.GET.get('teacher_name') != None):
            query = self.request.GET.get('teacher_name')
            object_list = Classroom.objects.filter(Q(teacher_name__icontains=query))
        if(self.request.GET.get('grade') != None):
            query = self.request.GET.get('grade')
            object_list = Classroom.objects.filter(Q(grade__icontains=query))

        # Syntax for complex query with single input used to query across multiple database fields
        # query = self.request.GET.get('q')
        # object_list = Classroom.objects.filter(
        #     Q(teacher_name__icontains=query) | Q(state__icontains=query) | Q(district__icontains=query) | Q(grade__icontains=query)
        # )
        return object_list