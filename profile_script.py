import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')
django.setup()

from portfolio.models import Profile

# Create Profile with user's name
profile, created = Profile.objects.get_or_create(
    id=1,
    defaults={
        'full_name': 'Dwight Vandrew G. Geralde',
        'tagline': 'Information Technology Student',
        'about_text': """I am an IT student who is passionate about learning and exploring different areas of technology. I am currently developing my skills in programming and web development, and I am motivated to create practical and meaningful projects.""",
        'career_goals': 'My goal is to continue growing as a developer while contributing to meaningful projects that make a positive impact.',
        'email': 'dwightgeralde69@gmail.com',
        'phone': '+1 (555) 123-4567',
        'location': 'Bayawan City, Neg. Or.',
        'github_url': 'https://github.com/dwightgeralde',
        'linkedin_url': 'https://linkedin.com/in/dwightgeralde',
        'twitter_url': 'https://twitter.com/dwightgeralde',
        'website_url': 'https://dwightgeralde.com',
    }
)

print(f"Profile for '{profile.full_name}' {'created' if created else 'already exists'}")

# Update tagline, about_text, location, email and clear social links
profile.tagline = 'Information Technology student'
profile.about_text = """I am an IT student who is passionate about learning and exploring different areas of technology. I am currently developing my skills in programming and web development, and I am motivated to create practical and meaningful projects."""
profile.location = 'Bayawan City, Neg. Or.'
profile.email = 'dwightgeralde69@gmail.com'
profile.career_goals = ''
profile.linkedin_url = ''
profile.twitter_url = ''
profile.save()
print(f"Tagline updated to: '{profile.tagline}'")
print(f"About text updated successfully")
print(f"Location updated to: '{profile.location}'")
print(f"Email updated to: '{profile.email}'")
print(f"Career goals cleared")
print(f"LinkedIn and Twitter removed")
