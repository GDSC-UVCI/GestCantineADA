from django.urls import path
from cantine.views.menu_views import menu_list, menu_add_and_edit
from cantine.views.dishe_views import dishes_list, dishes_add_and_edit, dishes_delete

app_name = 'cantine'

urlpatterns = [
    path('menus/', menu_list, name='menus_list'),
    path('menus/add/', menu_add_and_edit, name='menu_add'),
    path('menus/edit/<int:pk>/', menu_add_and_edit, name='menu_edit'),
    path('menus/delete/<int:pk>/', menu_add_and_edit, name='menu_delete'),
    path('dishes/', dishes_list, name='dishes_list'),
    path('dishes/add/', dishes_add_and_edit, name='dishes_add'),
    path('dishes/edit/<int:pk>/', dishes_add_and_edit, name='dishes_edit'),
    path('dishes/delete/<int:pk>/', dishes_delete, name='dishes_delete'),
    ]