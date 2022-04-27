from django.urls import path
from finalapp import views

urlpatterns = [

path('welcome',views.welcome,name='welcome'),
path('load_form',views.load_form,name='load_form'),
path('add',views.add,name='add'),
path('show',views.show,name='show'),
path('edit/<int:id>',views.edit,name='edit'),
path('edit/update/<int:id>',views.update,name='update'),
path('delete/<int:id>',views.delete,name='delete'),
path('search',views.search,name='search'),

]
