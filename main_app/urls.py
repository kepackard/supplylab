from django.urls import path
from . import views

urlpatterns = [
    # ========== GENERAL Routes ==========
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # ========== AUTHENTICATION Routes ==========
    path('classroom/', views.classroom_index, name='classroom_index'),


    # ========== CLASSROOM Routes ==========


    # ========== ITEM Routes ==========

    # ========== WISHLIST Routes ==========
    # ----- (associating Items to classroom)
]