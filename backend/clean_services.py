import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proforma_backend.settings')
django.setup()

from core.models import Service

def clean_services():
    """Clean up services with invalid feature data"""
    
    services = Service.objects.all()
    
    for service in services:
        print(f"\nChecking service: {service.title}")
        print(f"  Features type: {type(service.features)}")
        print(f"  Features: {service.features}")
        
        # If features is a list of objects, convert to list of strings
        if isinstance(service.features, list) and len(service.features) > 0:
            if isinstance(service.features[0], dict):
                print(f"  Converting object features to strings...")
                service.features = [f.get('title', f.get('name', str(f))) for f in service.features]
                service.save()
                print(f"  ✓ Converted to: {service.features}")
        
        # Ensure services_list is a list of strings
        if isinstance(service.services_list, list) and len(service.services_list) > 0:
            if isinstance(service.services_list[0], dict):
                print(f"  Converting object services_list to strings...")
                service.services_list = [s.get('title', s.get('name', str(s))) for s in service.services_list]
                service.save()
                print(f"  ✓ Converted services_list")
    
    print("\n✓ All services cleaned!")

if __name__ == '__main__':
    clean_services()
