import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proforma_backend.settings')
django.setup()

from core.models import HomePageService

def populate_homepage_services():
    """Populate homepage services"""
    
    # Delete existing data
    HomePageService.objects.all().delete()
    
    services_data = [
        {
            'title': 'Accounting Services',
            'subtitle': 'Professional bookkeeping and financial management solutions',
            'icon_name': 'Calculator',
            'order': 1,
            'is_active': True,
        },
        {
            'title': 'Tax Planning',
            'subtitle': 'Strategic tax planning and compliance services',
            'icon_name': 'FileText',
            'order': 2,
            'is_active': True,
        },
        {
            'title': 'IT Solutions',
            'subtitle': 'Comprehensive IT infrastructure and support services',
            'icon_name': 'Monitor',
            'order': 3,
            'is_active': True,
        },
        {
            'title': 'Digital Marketing',
            'subtitle': 'Data-driven digital marketing strategies',
            'icon_name': 'TrendingUp',
            'order': 4,
            'is_active': True,
        },
        {
            'title': 'Cloud Services',
            'subtitle': 'Secure cloud migration and management',
            'icon_name': 'Cloud',
            'order': 5,
            'is_active': True,
        },
        {
            'title': 'Cybersecurity',
            'subtitle': 'Advanced security solutions for your business',
            'icon_name': 'Shield',
            'order': 6,
            'is_active': True,
        },
    ]
    
    created_services = []
    for service_data in services_data:
        service = HomePageService.objects.create(**service_data)
        created_services.append(service)
        print(f"✓ Created service: {service.title}")
    
    return created_services

if __name__ == '__main__':
    print("Populating homepage services...")
    services = populate_homepage_services()
    print(f"\n✓ Successfully created {len(services)} homepage services!")
    print("\nNote: Please add images manually through the Django admin panel at:")
    print("http://localhost:8000/admin/core/homepageservice/")
