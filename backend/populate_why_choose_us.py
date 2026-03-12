import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proforma_backend.settings')
django.setup()

from core.models import WhyChooseUs

def populate_why_choose_us():
    """Populate WhyChooseUs section with sample data"""
    
    # Delete existing data
    WhyChooseUs.objects.all().delete()
    
    # Create WhyChooseUs content
    why_choose_us = WhyChooseUs.objects.create(
        key_advantages=[
            "Deep understanding of Nepali business landscape",
            "Experienced team of certified professionals",
            "Personalized solutions tailored to your needs",
            "Proven track record of client success",
            "Comprehensive service offerings under one roof",
            "Commitment to excellence and integrity"
        ],
        partner_title="Your Trusted Partner",
        partner_description="We combine deep industry knowledge with innovative solutions to deliver exceptional value to our clients. Our team of experts is dedicated to understanding your unique challenges and providing customized strategies that drive real results.",
        numbered_points=[
            {
                "title": "Expert Guidance",
                "description": "Professional advice from experienced consultants with decades of combined expertise"
            },
            {
                "title": "Innovative Solutions",
                "description": "Cutting-edge approaches to business challenges using the latest technology and methodologies"
            },
            {
                "title": "Client-Centric Approach",
                "description": "We prioritize your success and work collaboratively to achieve your business goals"
            },
            {
                "title": "Proven Results",
                "description": "Track record of helping businesses grow and succeed in competitive markets"
            }
        ]
    )
    
    print("✅ WhyChooseUs section populated successfully!")
    print(f"   - {len(why_choose_us.key_advantages)} key advantages")
    print(f"   - {len(why_choose_us.numbered_points)} numbered points")

if __name__ == '__main__':
    populate_why_choose_us()
