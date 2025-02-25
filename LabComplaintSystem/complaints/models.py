from django.db import models

# Create your models here.
from django.db import models
from users.models import UserProfile
from django.db import models
from users.models import UserProfile

class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('equipment', 'Equipment'),
        ('software', 'Software'),
        ('safety', 'Safety'),
        ('other', 'Other'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='created_complaints')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_complaints')

    def __str__(self):
        return self.title
    
from django.db import models
from users.models import UserProfile

class Comment(models.Model):
    complaint = models.ForeignKey('Complaint', on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    commented_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.commented_by.username} on {self.complaint.title}"