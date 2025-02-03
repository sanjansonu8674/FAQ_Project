This project is a multilingual FAQ management system built with Django (backend) and React (frontend) "But unfortunately, I could not create a front end" means that while trying to develop a website or application, you were unable to build the visible user interface (UI) part. It supports a WYSIWYG editor for rich text answers and provides API-based access to FAQs with language selection.

Features

Django Models with Multilingual Support
WYSIWYG Editor (django-ckeditor)
REST API for FAQs (Supports ?lang= parameter)
Redis-based Caching for Performance
Automated Translations using Google Translate
Admin Panel for Managing FAQs
Unit Tests (pytest)
Docker & Docker Compose Support
Deployment Ready (Heroku/AWS)
Installation Steps

1. Set Up a Virtual Environment

python -m venv venv source venv/bin/activate # On Windows: venv\Scripts\activate

2. Install Dependencies

pip install -r requirements.txt

3.Set Up Environment Variables

Create a .env file in the root directory:

SECRET_KEY=your-secret-key
DEBUG=True
REDIS_URL=redis://localhost:6379/1
4. Set Up the Database

python manage.py makemigrations python manage.py migrate

5. Create a Superuser for Admin Access

python manage.py createsuperuser

6. Start the Development Server python manage.py runserver

API Usage Examples

1️. Fetch All FAQs (Default: English)

http://localhost:8000/api/faqs/

2️. Fetch FAQs in Hindi

http://localhost:8000/api/faqs/?lang=hi

Fetch FAQs in Bengali
http://localhost:8000/api/faqs/?lang=bn

4️. Create a New FAQ (POST Request) { "question": "What is Django?", "answer": "Django is a web framework." }
