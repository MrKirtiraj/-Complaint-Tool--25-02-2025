from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('file_complaint/', views.dashboard, name='file_complaint'),
    path('complaints/', include('complaints.urls')),
    path('complaints/', include('complaints.urls')),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('', views.home, name='home'),  # Home page URL
]


# kbtug22115 : kirtiRAJ123 : abc@xyz.com        Student
# teach1 : myteacheris1 : teach1@gmail.com      staff
# admin : myadminis1 : admin@gmail.com          admin