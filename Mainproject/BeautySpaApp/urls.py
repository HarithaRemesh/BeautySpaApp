from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage,name='home'),
    path('accounts/login',views.logfunc,name='login'),
    path('specpage',views.spec,name='spec'),
    path('book_appointment',views.book_appointment, name="book_appointment"),
    path('status_check',views.status_check,name='status_check'),
    path('contact',views.contactpage,name='contact'),
    path('thankyou',views.thankyoupage, name='thankyou')

 ]