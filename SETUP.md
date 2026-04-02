# Django Portfolio - Quick Start Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup Instructions

### 1. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

The `.env` file is already created with default values. For production, update the values:

```
DEBUG=False
SECRET_KEY=your-secure-random-key-here
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### 4. Run Database Migrations

```bash
python manage.py migrate
```

### 5. Populate Sample Data (Optional)

To populate the database with sample content:

```bash
python manage.py shell < portfolio/migrations/populate_data.py
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to view your portfolio.

## Customizing Your Portfolio

### Using the Admin Panel

1. Go to http://127.0.0.1:8000/admin/
2. Log in with your superuser credentials
3. You can manage:
   - **Profile**: Your personal information, photo, social links
   - **Skills**: Add technical skills organized by category
   - **Projects**: Showcase your work with descriptions and links
   - **Education**: Your academic background
   - **Contact Messages**: View messages from visitors

### Adding Your Profile Photo

1. Go to admin panel → Profiles
2. Edit the profile and upload your photo (recommended: square image, 500x500px)

### Adding Projects

For each project, you can:
- Add a title and description
- List technologies used
- Link to GitHub repository
- Link to live demo
- Upload a project screenshot
- Mark as "featured" to show on homepage

## Project Structure

```
portfolio/
├── portfolio_project/    # Django settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/           # Main app
│   ├── models.py       # Data models
│   ├── views.py        # Page views
│   ├── urls.py         # URL routing
│   ├── admin.py        # Admin configuration
│   ├── forms.py        # Contact form
│   └── templates/      # HTML templates
├── static/             # CSS, JS, images
│   └── css/
│       └── style.css
├── media/              # User uploads
├── manage.py           # Django commands
├── requirements.txt    # Dependencies
└── README.md          # Documentation
```

## Deployment

For production deployment:

1. Set `DEBUG=False` in `.env`
2. Use a production-ready database (PostgreSQL recommended)
3. Collect static files: `python manage.py collectstatic`
4. Use a production WSGI server (Gunicorn/uWSGI)
5. Configure a reverse proxy (Nginx/Apache)

## Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Dynamic Content**: All content managed via Django admin
- **Contact Form**: Visitors can send messages directly
- **SEO Friendly**: Proper meta tags and semantic HTML
- **Social Integration**: Links to GitHub, LinkedIn, Twitter
- **Modern UI**: Bootstrap 5 with custom styling

## Support

For issues or questions, please check the Django documentation or create an issue in the repository.
