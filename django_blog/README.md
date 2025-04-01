# Django Blog Authentication System

## Features
- User Registration
- Login / Logout
- Profile Management
- Secure Authentication with CSRF Protection

## Setup Instructions
1. Clone the repository:
2. Navigate to the `django_blog` directory:
3. Install dependencies:
4. Apply migrations:
5. Create a superuser:
6. Run the development server:

Visit `http://127.0.0.1:8000/` to access the application.

## Usage
- Register: `/register/`
- Login: `/login/`
- Logout: `/logout/`
- Profile: `/profile/`


# Django Blog - CRUD Functionality

## Features
- Create, Read, Update, and Delete blog posts
- User authentication to restrict access
- Secure editing/deletion (Only post authors can modify their posts)

## Setup Instructions
1. Clone the repository:
   git clone https://github.com/yourusername/Alx_DjangoLearnLab.git

2. Navigate to the project directory:
cd django_blog

3. Install dependencies:
pip install -r requirements.txt

4. Apply database migrations:
python manage.py migrate

5. Create a superuser:
python manage.py createsuperuser
6. Run the development server:
python manage.py runserver
7. Open the application:

Blog List: http://127.0.0.1:8000/

Create Post: http://127.0.0.1:8000/post/new/

View Post: http://127.0.0.1:8000/post/<id>/

Edit Post: http://127.0.0.1:8000/post/<id>/edit/

Delete Post: http://127.0.0.1:8000/post/<id>/delete/

8. Permissions
Authenticated users can create posts.

Post authors can edit or delete their own posts.

All users (even unauthenticated) can view posts.