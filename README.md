# Fashion Hub ATP — Boutique Fashion Store

A modern, elegant Django web application for **SRI LAKSHMI CHENNKASHEVA FANCY STORE** featuring a beautiful girlish design with soft pink aesthetics.

## Store Information

- **Store Name:** SRI LAKSHMI CHENNKASHEVA FANCY STORE
- **Location:** KLD Bypass, Pampeta, Behind Hanuman Temple, Anantapur
- **Contact:** 7013821498

## Features

### Admin Features
- Full product management (Add, Edit, Delete)
- Category management
- Image upload with Cloudinary support
- Django admin panel at `/admin`

### Public Features
- Browse all products without login
- Filter by category
- Search products
- Responsive mobile-first design
- Elegant pink-themed UI
- Smooth animations and hover effects

## Categories

1. Dress (Women)
2. Dress Materials
3. Blouse Pieces
4. Sarees
5. Cosmetics
6. Bangles
7. Fancy Items (Chains, Necklaces, Bracelets)
8. Hair Accessories
9. Innerwears
10. Others
11. Kids Play Arena
12. Kids Clothing

## Tech Stack

- **Backend:** Django 6.0
- **Database:** PostgreSQL (production) / SQLite (development)
- **Media Storage:** Cloudinary
- **Frontend:** HTML, CSS, Bootstrap 5
- **Deployment:** Render-ready

## Local Development Setup

### Prerequisites
- Python 3.10+
- pip

### Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Seed categories:
```bash
python manage.py seed_categories
```

5. Create admin user (username: KVL@2005, password: 5002):
```bash
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('KVL@2005', '', '5002')
"
```

6. Collect static files:
```bash
python manage.py collectstatic --no-input
```

7. Run development server:
```bash
python manage.py runserver
```

8. Access the site:
- Homepage: http://localhost:8000
- Admin: http://localhost:8000/admin

## Deployment to Render

### Step 1: Setup Cloudinary
1. Sign up at https://cloudinary.com
2. Get your Cloud Name, API Key, and API Secret from the dashboard

### Step 2: Deploy to Render
1. Push code to GitHub
2. Create new Web Service on Render
3. Connect your GitHub repository
4. Render will auto-detect `render.yaml`
5. Add environment variables in Render dashboard:
   - `CLOUDINARY_CLOUD_NAME`
   - `CLOUDINARY_API_KEY`
   - `CLOUDINARY_API_SECRET`
6. Deploy!

### Step 3: Create Admin User on Render
After first deployment, run in Render Shell:
```bash
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('KVL@2005', '', '5002')
"
```

## Project Structure

```
fashionhub/
├── fashionhub/          # Project settings
│   ├── settings.py      # Main configuration
│   ├── urls.py          # URL routing
│   └── wsgi.py          # WSGI config
├── store/               # Main app
│   ├── models.py        # Category & Product models
│   ├── views.py         # View logic
│   ├── admin.py         # Admin configuration
│   ├── urls.py          # App URLs
│   └── management/      # Custom commands
├── templates/           # HTML templates
│   └── store/
│       ├── base.html
│       ├── home.html
│       ├── category.html
│       ├── all_products.html
│       └── contact.html
├── static/              # CSS & JS
│   ├── css/style.css
│   └── js/main.js
├── media/               # Uploaded images (local dev)
├── requirements.txt     # Python dependencies
├── build.sh            # Render build script
└── render.yaml         # Render configuration
```

## Database Models

### Category
- `name` (CharField, unique)

### Product
- `name` (CharField)
- `category` (ForeignKey to Category)
- `price` (DecimalField)
- `description` (TextField, optional)
- `image` (ImageField)
- `created_at` (DateTimeField, auto)

## Design Theme

- **Primary Color:** #f8c8dc (light pink)
- **Secondary Color:** #f5e6e8 (blush)
- **Accent Color:** #d63384 (deep pink)
- **Fonts:** Playfair Display (headings), Poppins (body)

## Important Notes

- Admin credentials are NOT stored in code for security
- Use PostgreSQL in production (configured via DATABASE_URL)
- Cloudinary handles media storage in production
- WhiteNoise serves static files efficiently
- All 12 categories are auto-seeded on deployment

## Support

For issues or questions, contact: 7013821498

---

Built with ❤️ for SRI LAKSHMI CHENNKASHEVA FANCY STORE
