from django.urls import path
from . import views

from fac.views import list_fac_view, update_fac_view, delete_fac

urlpatterns = [
    path('import-fac/',views.upload_fac, name ='import-fac'),
    path('act_load_fac/',views.act_load_fac, name ='act_load_fac'),
    path('create_fac/', views.create_fac, name='create_fac'),
 
    path('list_fac/', views.list_fac_view, name='list-fac'), # Funcion

    path('find_fac/', views.find_fac, name='find_fac'),

    path('del_fac/<int:id>/',views.delete_fac, name='del_fac'),

    path('update-fac-view/<int:id>', update_fac_view.as_view(), name='update_fac_view'),
 
]
