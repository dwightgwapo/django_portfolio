# Django Portfolio Project

A professional portfolio website built with Django.

## Features

- **Home Page**: Introduction with profile photo and navigation
- **About Section**: Personal background and career goals
- **Skills Section**: Technical and professional skills with categories
- **Projects Section**: Showcase of projects with descriptions and links
- **Education Section**: Academic background
- **Contact Section**: Contact form and social links

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file in the project root:
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the admin panel at `/admin` to add your content.

## Project Structure

```
portfolio/
├── portfolio_project/    # Django project settings
├── portfolio/           # Main portfolio app
│   ├── models.py       # Data models
│   ├── views.py        # View functions
│   ├── urls.py         # URL patterns
│   └── templates/      # HTML templates
├── static/             # Static files (CSS, JS, images)
├── media/              # User uploaded files
└── manage.py           # Django management script
```
