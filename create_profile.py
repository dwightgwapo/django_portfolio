"""
Create profile with user's name for the portfolio.
Run: python manage.py shell < create_profile.py
"""
from portfolio.models import Profile

# Create Profile with user's name
profile, created = Profile.objects.get_or_create(
    id=1,
    defaults={
        'full_name': 'Dwight Vandrew G. Geralde',
        'tagline': 'Full-Stack Developer | Python & Django Specialist',
        'about_text': """I'm a passionate full-stack developer with a strong focus on creating efficient, scalable web applications. With expertise in Python and Django, I enjoy solving complex problems and turning ideas into reality through code.

My journey in software development started with a curiosity about how things work on the web. That curiosity evolved into a career where I've had the opportunity to work on diverse projects, from e-commerce platforms to data analytics dashboards.

I believe in writing clean, maintainable code and following best practices. I'm always eager to learn new technologies and improve my skills.""",
        'career_goals': 'My goal is to continue growing as a developer while contributing to meaningful projects that make a positive impact.',
        'email': 'dwight.geralde@example.com',
        'phone': '+1 (555) 123-4567',
        'location': 'San Francisco, CA',
        'github_url': 'https://github.com/dwightgeralde',
        'linkedin_url': 'https://linkedin.com/in/dwightgeralde',
        'twitter_url': 'https://twitter.com/dwightgeralde',
        'website_url': 'https://dwightgeralde.com',
    }
)

print(f"Profile for '{profile.full_name}' {'created' if created else 'already exists'}")
