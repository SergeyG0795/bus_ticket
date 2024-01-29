from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from ticket_reservation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.schedule, name='schedule'),
    path('reserve/<int:bus_id>/', views.reserve_ticket, name='reserve_ticket'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('login/', views.login, name='login'),
    # path('register/', views.register, name='register')
]
