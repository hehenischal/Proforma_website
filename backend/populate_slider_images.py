"""
Script to populate slider images
Run with: python manage.py shell < populate_slider_images.py
Or: Get-Content populate_slider_images.py | python manage.py shell
"""

from core.models import SliderImage

print("=" * 60)
print("POPULATING SLIDER IMAGES")
print("=" * 60)

# Note: Since we don't have actual image files, we'll create entries
# You'll need to upload images via the admin panel

slider_data = [
    {
        "title": "Welcome to Proforma",
        "subtitle": "Professional Solutions for Your Success",
        "button_text": "Learn More",
        "button_link": "/about",
        "order": 1,
        "is_active": True
    },
    {
        "title": "Expert Accounting Services",
        "subtitle": "Comprehensive financial solutions tailored to your needs",
        "button_text": "Our Services",
        "button_link": "/services",
        "order": 2,
        "is_active": True
    },
    {
        "title": "Digital Transformation",
        "subtitle": "Innovative IT solutions for modern businesses",
        "button_text": "Explore IT Services",
        "button_link": "/services/it",
        "order": 3,
        "is_active": True
    },
    {
        "title": "Tax Planning & Compliance",
        "subtitle": "Strategic tax solutions to optimize your business",
        "button_text": "Tax Services",
        "button_link": "/services/tax",
        "order": 4,
        "is_active": True
    },
]

for data in slider_data:
    slider, created = SliderImage.objects.update_or_create(
        title=data['title'],
        defaults=data
    )
    print(f"  {'Created' if created else 'Updated'}: {slider.title}")

print(f"\nTotal active slider images: {SliderImage.objects.filter(is_active=True).count()}")
print("\n" + "=" * 60)
print("IMPORTANT: Upload images via admin panel")
print("Admin URL: http://localhost:8000/admin/core/sliderimage/")
print("=" * 60)
