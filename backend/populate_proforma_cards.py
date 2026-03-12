import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proforma_backend.settings')
django.setup()

from core.models import ProformaCard

def populate_proforma_cards():
    """Populate ProformaCard model with sample data"""
    
    # Clear existing cards
    ProformaCard.objects.all().delete()
    print("Cleared existing Proforma cards")
    
    cards_data = [
        {
            'title': 'Our Mission',
            'slug': 'our-mission',
            'icon_name': 'Crosshair',
            'content_blocks': [
                {
                    'type': 'paragraph',
                    'content': 'At Proforma Insights, our mission is to empower businesses with expert consultancy and innovative IT solutions that drive growth and efficiency.'
                },
                {
                    'type': 'list',
                    'content': [
                        'Empower businesses with expert consultancy',
                        'Provide innovative IT solutions',
                        'Drive growth and efficiency',
                        'Ensure success in the digital landscape'
                    ]
                }
            ],
            'order': 1,
            'is_active': True
        },
        {
            'title': 'Benefits',
            'slug': 'benefits',
            'icon_name': 'Star',
            'content_blocks': [
                {
                    'type': 'paragraph',
                    'content': 'Partnering with Proforma Insights brings numerous advantages to your business.'
                },
                {
                    'type': 'list',
                    'content': [
                        'Expertise: Seasoned consultants with industry knowledge',
                        'Customized Solutions: Tailored services for your needs',
                        'Comprehensive Services: All solutions under one roof',
                        'Client-Centric Approach: Your success is our priority'
                    ]
                }
            ],
            'order': 2,
            'is_active': True
        },
        {
            'title': 'Our Goal',
            'slug': 'our-goal',
            'icon_name': 'Rocket',
            'content_blocks': [
                {
                    'type': 'paragraph',
                    'content': 'We aim to be the leading provider of business and IT consultancy services in Nepal and beyond.'
                },
                {
                    'type': 'list',
                    'content': [
                        'Leading provider of consultancy services',
                        'Recognized for excellence and innovation',
                        'Build long-term partnerships with clients',
                        'Help businesses navigate challenges successfully'
                    ]
                }
            ],
            'order': 3,
            'is_active': True
        }
    ]
    
    created_count = 0
    for card_data in cards_data:
        card = ProformaCard.objects.create(**card_data)
        created_count += 1
        print(f"✓ Created: {card.title}")
    
    print(f"\n✅ Successfully created {created_count} Proforma cards!")
    print("\nYou can now:")
    print("1. View them at: http://localhost:8000/api/proforma-cards/")
    print("2. Edit them in Django admin: http://localhost:8000/admin/core/proformacard/")
    print("3. Add images to each card in the admin panel")

if __name__ == '__main__':
    populate_proforma_cards()
