"""Models for the portfolio app."""
from django.db import models


class SkillCategory(models.Model):
    """Category for grouping skills."""
    name = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Skill Categories'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Technical or professional skill."""
    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    proficiency = models.PositiveSmallIntegerField(default=50, help_text='Proficiency level 0-100')
    icon = models.CharField(max_length=50, blank=True, help_text='Font Awesome icon class (optional)')

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Education(models.Model):
    """Educational background."""
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False, help_text='Check if currently studying')
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='education/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Education'
        ordering = ['-end_date', '-start_date']

    def __str__(self):
        return f"{self.degree} at {self.institution}"

    def get_duration(self):
        if self.is_current or not self.end_date:
            return f"{self.start_date.year} - Present"
        return f"{self.start_date.year} - {self.end_date.year}"


class Project(models.Model):
    """Portfolio project."""
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, help_text='Comma-separated list of technologies')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateField()
    is_featured = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def get_technology_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]


class ContactMessage(models.Model):
    """Contact form submissions."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


class Profile(models.Model):
    """Personal profile information."""
    full_name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    about_text = models.TextField()
    career_goals = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
