
from django.urls import path

from ToDoApp import views

urlpatterns=[
    path('',views.NewOne,name='NewOne'),
    path('dash',views.dash,name='dash'),
path('',views.dash,name='dash'),
    path('NotFound',views.NotFound,name='NotFound'),
    path('blank',views.blank,name='blank'),
    path('button',views.button,name='button'),
    path('chart',views.chart,name='chart'),
    path('element',views.element,name='element'),
    path('form',views.form,name='form'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('table',views.table,name='table'),
    path('typography',views.typography,name='typography'),
    path('widget',views.widget,name='widget'),


    path('addData',views.addData,name='addData'),
    path('view',views.view,name='view'),
    path('dbn',views.dbn,name='dbn'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),


]