# Techternet - Modern Tech Blog Platform

## Overview
Techternet is a modern, responsive tech blog platform inspired by TechCrunch. Built with Django and HTML/CSS, it features a beautiful design with Tech Scarlet (#E63946) as the primary accent color, paired with Deep Navy Black (#0D1117) and Soft White (#F5F5F5) for a clean, high-contrast interface.

## Recent Changes
- **October 31, 2025**: Initial setup and implementation
  - Created Django project with blog app
  - Implemented Post and Category models with full admin interface
  - Designed responsive homepage with featured articles grid
  - Built article detail pages with SEO optimization
  - Added category browsing and pagination
  - Created modern CSS with Tech Scarlet color scheme and gradient hover effects
  - Implemented SEO meta tags and Open Graph tags
  - Set up media handling for post images

## Project Architecture

### Backend (Django)
- **Framework**: Django 5.2.7
- **Database**: PostgreSQL (production-ready)
- **Apps**:
  - `blog`: Main app handling posts, categories, and views

### Models
- **Post**: Title, slug, author, category, featured image, excerpt, content, publishing status, SEO fields
- **Category**: Name, slug, description for organizing articles

### Frontend
- **Templates**: HTML5 with Django template engine
- **Styling**: Custom CSS with modern design system
- **Font**: Inter (Google Fonts)
- **Color Scheme**:
  - Primary: #E63946 (Tech Scarlet)
  - Primary Dark: #C1121F
  - Background Dark: #0D1117
  - Background Light: #F5F5F5

### Key Features
1. **Homepage**: Hero section, featured articles (up to 3), latest articles grid (12), category cards
2. **Article Detail**: Full post with featured image, author info, publish date, views counter, related articles
3. **Category Pages**: Filtered articles with pagination (12 per page)
4. **Admin Panel**: Full CRUD operations for posts and categories
5. **SEO**: Meta descriptions, Open Graph tags, semantic HTML
6. **Responsive**: Mobile-first design with breakpoints at 768px and 480px

## Getting Started

### Creating an Admin User
Run the helper script to create an admin account:
```bash
python create_admin.py
```

Or use Django's built-in command:
```bash
python manage.py createsuperuser
```

### Accessing the Admin Panel
1. Navigate to `/admin/` in your browser
2. Login with your admin credentials
3. Start creating categories and posts!

### Creating Your First Post
1. Go to the admin panel
2. Add a Category (e.g., "AI & Machine Learning", "Startups", "Hardware")
3. Click "Posts" → "Add Post"
4. Fill in:
   - Title (slug auto-generates)
   - Author (automatically set to logged-in user)
   - Category
   - Excerpt (brief summary, max 300 chars)
   - Content (full article text)
   - Featured Image (optional)
   - Check "Is published" to make it live
   - Check "Is featured" to show on homepage featured section
5. Save!

## File Structure
```
techternet/
├── blog/                   # Main blog app
│   ├── models.py          # Post and Category models
│   ├── views.py           # View functions
│   ├── admin.py           # Admin configuration
│   ├── urls.py            # Blog URL patterns
│   └── templates/blog/    # HTML templates
│       ├── base.html      # Base template
│       ├── home.html      # Homepage
│       ├── post_detail.html
│       └── category.html
├── techternet/            # Project settings
│   ├── settings.py        # Django settings
│   └── urls.py            # Main URL config
├── static/css/            # Static CSS files
│   └── style.css          # Main stylesheet
├── media/posts/           # Uploaded images
├── manage.py              # Django management script
└── create_admin.py        # Helper script for admin creation

## Design System

### Colors
- **Tech Scarlet**: #E63946 (primary accent, CTAs, categories)
- **Scarlet Dark**: #C1121F (gradient end)
- **Deep Navy Black**: #0D1117 (header backgrounds, text)
- **Soft White**: #F5F5F5 (page background)
- **Text Gray**: #6B7280 (secondary text)

### Typography
- **Font Family**: Inter
- **Headings**: 700-800 weight
- **Body**: 400-500 weight
- **Hero Title**: 56px (mobile: 28px)
- **Section Title**: 32px (mobile: 28px)
- **Card Title**: 20px

### Components
- **CTA Buttons**: Linear gradient with hover lift effect
- **Cards**: Shadow on hover, rounded corners (12-16px)
- **Navigation**: Sticky header with backdrop blur
- **Grid**: CSS Grid for responsive layouts

## SEO Optimization
- Meta descriptions (auto-generated from excerpt if not provided)
- Open Graph tags for social media sharing
- Semantic HTML5 structure
- Clean URL slugs (auto-generated from titles)
- Article schema with author and publish dates

## User Preferences
- Modern, clean design aesthetic
- TechCrunch-inspired layout
- High responsiveness across all devices
- SEO-optimized for discoverability
- Easy content management through Django admin
```
