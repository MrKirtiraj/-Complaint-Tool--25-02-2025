from django.contrib import admin

# # Register your models here.
# from complaints.models import Complaint, Comment
# class Complaint_admin1(admin.ModelAdmin):
#     list_display = ("CATEGORY_CHOICES","PRIORITY_CHOICES", "title", "description" )

# admin.site.register(Complaint, Complaint_admin1)

# class Comment_admin1(admin.ModelAdmin):
#     list_display= ("complaint", "comment")
# admin.site.register(Comment, Comment_admin1)


from django.contrib import admin
from .models import Complaint, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('complaint', 'commented_by', 'commented_at', 'comment')
    list_filter = ('commented_at', 'commented_by')
    search_fields = ('comment', 'complaint__title')

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'priority', 'status', 'created_by', 'assigned_to', 'created_at')
    list_filter = ('status', 'category', 'priority')
    search_fields = ('title', 'description')