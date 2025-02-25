from django.shortcuts import render

from complaints.models import Complaint

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('dashboard')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         # Add login logic here
#         pass
#     return render(request, 'users/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'users/home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')

from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from complaints.models import Complaint



#old code:
"""
@login_required
def dashboard(request):
    user = request.user
    if user.role == 'student':
        # Students see their own complaints
        complaints = Complaint.objects.filter(created_by=user)
    elif user.role == 'staff':
        # Staff see complaints assigned to them
        complaints = Complaint.objects.all()
    elif user.role == 'admin':
        # Admins see all complaints
        complaints = Complaint.objects.all()
    else:
        complaints = []

    context = {
        'complaints': complaints,
        'user_role': user.role,
    }
    return render(request, 'users/dashboard.html', context)
"""

#new code of dashboard:
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from complaints.models import Complaint

@login_required
def dashboard(request):
    user = request.user
    complaints = Complaint.objects.all()

    # Filtering
    status_filter = request.GET.get('status')
    category_filter = request.GET.get('category')
    priority_filter = request.GET.get('priority')

    if status_filter:
        complaints = complaints.filter(status=status_filter)
    if category_filter:
        complaints = complaints.filter(category=category_filter)
    if priority_filter:
        complaints = complaints.filter(priority=priority_filter)

    # Sorting
    sort_by = request.GET.get('sort_by')
    if sort_by == 'created_at':
        complaints = complaints.order_by('created_at')
    elif sort_by == 'priority':
        complaints = complaints.order_by('priority')

    if user.role == 'student':
        complaints = complaints.filter(created_by=user)
    elif user.role == 'staff':
        complaints = complaints.all()

    context = {
        'complaints': complaints,
        'user_role': user.role,
    }
    return render(request, 'users/dashboard.html', context)


from django.core.mail import send_mail
from django.conf import settings

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Send an email (optional)
        send_mail(
            subject=f"Contact Us Message from {name}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        return render(request, 'users/contact_us.html', {'success': True})
    return render(request, 'users/contact_us.html')