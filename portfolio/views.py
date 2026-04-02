"""Views for the portfolio app."""
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, SkillCategory, Project, Education, ContactMessage
from .forms import ContactForm


def home(request):
    """Home page view."""
    profile = Profile.objects.first()
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    if not featured_projects:
        featured_projects = Project.objects.all()[:3]
    
    context = {
        'profile': profile,
        'featured_projects': featured_projects,
    }
    return render(request, 'portfolio/home.html', context)


def about(request):
    """About page view."""
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }
    return render(request, 'portfolio/about.html', context)


def skills(request):
    """Skills page view."""
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    context = {
        'skill_categories': skill_categories,
    }
    return render(request, 'portfolio/skills.html', context)


def projects(request):
    """Projects page view."""
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects,
    }
    return render(request, 'portfolio/projects.html', context)


def education(request):
    """Education page view."""
    education_list = Education.objects.all()
    context = {
        'education_list': education_list,
    }
    return render(request, 'portfolio/education.html', context)


def contact(request):
    """Contact page view with form."""
    profile = Profile.objects.first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)
