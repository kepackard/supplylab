from django.urls import path
from . import views

urlpatterns = [
    # ========== GENERAL Routes ==========
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('classrooms/', views.ClassroomIndex.as_view(), name='classroom_list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom_detail'),

    # ========== AUTHENTICATION Routes ==========
    path('accounts/signup/', views.signup, name='signup'),
    


    # ========== CLASSROOM Routes ==========


    # ========== ITEM Routes ==========

    # ========== WISHLIST Routes ==========
    # ----- (associating Items to classroom)
]