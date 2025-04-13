# Social Media API

A RESTful API for a social media platform built with Django and Django REST Framework. This version includes user registration, authentication using token-based auth, and user profile management.

---

## 🚀 Features

- User registration with token response
- Token-based login and authentication
- Custom user model with `bio`, `profile_picture`, and `followers`
- Profile view and update for authenticated users

---

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- DRF Token Authentication

---

## 📦 Installation

1. **Clone the repository**
   git clone https://github.com/YOUR_USERNAME/social_media_api.git
   cd social_media_api

2. **Create a virtual environment and activate it**
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install dependencies**
    pip install -r requirements.txt

4. **Apply migrations**
    python manage.py makemigrations
    python manage.py migrate

5. **Run the development server**
    python manage.py runserver

6. **🔐 API Authentication**
    The project uses Token Authentication provided by DRF.

7. **📮 API Endpoints**
Method	        Endpoint	        Description	Auth Required
POST	        /api/register/	    Register a new user	❌
POST	        /api/login/	        Log in and get token	❌
GET	            /api/profile/	    View authenticated profile	✅
PUT	            /api/profile/	    Update profile (bio, pic)	✅