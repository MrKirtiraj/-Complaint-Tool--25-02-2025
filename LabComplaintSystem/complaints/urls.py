from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('file/', views.file_complaint, name='file_complaint'),
    path('details/<int:complaint_id>/', views.complaint_details, name='complaint_details'),
]