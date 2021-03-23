from django.contrib import admin
from django.urls import path
from womenlab import views

urlpatterns = [
    
    path('',views.index, name='womenlab'),
    path('<int:id>/<str:slug>/', views.course_detail, name='course_detail'),
    path('<int:id>/<str:slug>/<int:price>/', views.pay_detail, name='pay_detail'),
    path('success', views.success, name='success'),
    path('<int:id>/',views.pay, name='pay')
]