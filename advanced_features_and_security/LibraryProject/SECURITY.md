# Security Measures Implemented in LibraryProject

## 1. Secure Django Settings
- Set `DEBUG=False` in production.
- Enabled `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS`, and `SECURE_CONTENT_TYPE_NOSNIFF`.
- Enforced secure cookies (`CSRF_COOKIE_SECURE=True`, `SESSION_COOKIE_SECURE=True`).

## 2. CSRF Protection
- `{% csrf_token %}` included in all forms.

## 3. Secure Data Handling
- Used Django ORM to prevent SQL injection.
- Added form validation to sanitize user input.

## 4. Content Security Policy (CSP)
- Implemented CSP via `django-csp` to restrict content sources.
