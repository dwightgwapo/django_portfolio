"""Admin configuration for the portfolio app."""
from django.contrib import admin
from .models import Profile, SkillCategory, Skill, Project, Education, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'location']
    search_fields = ['full_name', 'email']


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']
    ordering = ['order']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['category', 'name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'technologies', 'created_at', 'is_featured', 'order']
    list_filter = ['is_featured', 'created_at']
    list_editable = ['is_featured', 'order']
    search_fields = ['title', 'description']
    ordering = ['order', '-created_at']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['institution', 'degree', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current']
    search_fields = ['institution', 'degree']
    ordering = ['-end_date', '-start_date']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
