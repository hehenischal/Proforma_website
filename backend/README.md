# Proforma Insights Backend

Django REST API backend with Jazzmin admin panel for the Proforma Insights website.

## Features

- **Django 5.2** with Django REST Framework
- **Jazzmin Admin** - Beautiful admin interface
- **CORS enabled** for React frontend
- **SQLite database** (can be changed to PostgreSQL/MySQL)
- **Image upload** support with Pillow

## Models

- **Service** - Company services (Accounting, Tax, IT, Digital)
- **TeamMember** - Team member profiles
- **Insight** - Blog posts/articles
- **SliderImage** - Homepage slider images
- **CompanyStat** - Company statistics for counter
- **ContactInquiry** - Contact form submissions
- **CompanyInfo** - Company information (singleton)

## Setup

1. **Activate virtual environment:**
   ```bash
   .\venv\Scripts\activate
   ```

2. **Install dependencies** (already done):
   ```bash
   pip install django djangorestframework django-cors-headers django-jazzmin pillow
   ```

3. **Run migrations** (already done):
   ```bash
   python manage.py migrate
   ```

4. **Create superuser** (already done):
   - Username: `admin`
   - Password: `admin123`
   - Email: `admin@proforma.com`

5. **Start server:**
   ```bash
   python manage.py runserver 8000
   ```

## Access Points

- **Admin Panel**: http://localhost:8000/admin/
  - Login with: admin / admin123
  
- **API Endpoints**: http://localhost:8000/api/
  - `/api/services/` - List all services
  - `/api/team/` - List team members
  - `/api/insights/` - List insights/blog posts
  - `/api/slider/` - List slider images
  - `/api/stats/` - List company statistics
  - `/api/contact/` - Submit contact form (POST only)
  - `/api/company-info/current/` - Get company information

## API Usage

All GET endpoints are publicly accessible. The contact endpoint accepts POST requests.

Example API call:
```javascript
// Get all services
fetch('http://localhost:8000/api/services/')
  .then(res => res.json())
  .then(data => console.log(data));

// Submit contact form
fetch('http://localhost:8000/api/contact/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    first_name: 'John',
    last_name: 'Doe',
    email: 'john@example.com',
    phone: '1234567890',
    subject: 'Inquiry',
    message: 'Hello!'
  })
});
```

## Admin Panel Features

- Manage all content dynamically
- Upload images for services, team, insights, slider
- View and respond to contact inquiries
- Update company information
- Beautiful Jazzmin theme with custom icons
- Search functionality
- Bulk actions

## Next Steps

1. Log in to admin panel at http://localhost:8000/admin/
2. Add your services, team members, insights, etc.
3. Update the React frontend to fetch data from these APIs
4. Replace static content with dynamic API calls

## Production Deployment

For production:
1. Change `DEBUG = False` in settings.py
2. Set proper `ALLOWED_HOSTS`
3. Use PostgreSQL/MySQL instead of SQLite
4. Set up proper media/static file serving
5. Use environment variables for sensitive data
6. Set up HTTPS
