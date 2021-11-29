from django.urls import path
from . import views


urlpatterns = [
    # ========== GENERAL Routes ==========
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # ========== AUTHENTICATION Routes ==========
    path('accounts/signup/', views.signup, name='signup'),
    
    # ========== CLASSROOM Routes ==========
    path('classrooms/', views.ClassroomIndex.as_view(), name='classroom_list'),
    # path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom_detail'),      # Classroom Detail as function path
    path('classrooms/<int:pk>/', views.ClassroomDetail.as_view(), name='classroom_detail'),         # Classroom Detail as CBV
    path('classrooms/create/', views.ClassroomCreate.as_view(), name='classroom_create'),
    path('classrooms/<int:pk>/update/', views.ClassroomUpdate.as_view(), name='classroom_update'),
    path('classrooms/<int:pk>/delete/', views.ClassroomDelete.as_view(), name='classroom_delete'),
    path('classrooms/<int:classroom_id>/add_item/', views.add_item, name='add_item'),
   
    # ========== ITEM Routes ==========
    path('item/<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
    path('item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
    path('item/<int:pk>/update/', views.ItemUpdate.as_view(), name='item_update'),

    # ========== WISHLIST Routes ==========
    # ----- (associating Items to classroom)


    # ========== DONOR Routes ==========
]