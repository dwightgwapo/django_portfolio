"""
WSGI configuration for PythonAnywhere deployment.

This file should be used in the PythonAnywhere web app WSGI configuration.
Path on PythonAnywhere: /var/www/<your-domain>_wsgi.py

The project structure on PythonAnywhere should be:
/home/<username>/<project-name>/Web_Portfolio/portfolio/

Replace <username> and <project-name> with your actual values.
"""
import sys
import os

# Add your project directory to the sys.path
# Update this path to match your PythonAnywhere project location
# Example: /home/username/dwightgeralde/Web_Portfolio/portfolio
path = '/home/<username>/<project-folder>/Web_Portfolio/portfolio'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable to tell Django where your settings.py is
os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_project.settings'

# Serve Django app via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
