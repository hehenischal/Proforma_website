import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proforma_backend.settings')
django.setup()

from core.models import HomePage

def populate_homepage():
    """Populate homepage content"""
    
    # Delete existing data
    HomePage.objects.all().delete()
    
    # Create homepage content
    homepage = HomePage.objects.create(
        # Accounting Panel
        accounting_tag="Financial Services",
        accounting_title="Accounting & Tax Solutions",
        accounting_description="Expert bookkeeping, financial analysis, tax planning, and compliance management to keep your business financially sound and regulation-ready.",
        accounting_features=[
            {"icon": "BookOpen", "text": "Bookkeeping"},
            {"icon": "TrendingUp", "text": "Financial Analysis"},
            {"icon": "FileText", "text": "Tax Planning"},
            {"icon": "Shield", "text": "Compliance"}
        ],
        accounting_button1_text="Accounting Services",
        accounting_button1_link="/accounting",
        accounting_button2_text="Tax Services",
        accounting_button2_link="/tax",
        
        # IT Panel
        it_tag="Technology Solutions",
        it_title="IT & Digital Transformation",
        it_description="Strategic IT consulting, cybersecurity, cloud solutions, and digital marketing to accelerate your business into the future.",
        it_features=[
            {"icon": "Code", "text": "Software Dev"},
            {"icon": "Lock", "text": "Cybersecurity"},
            {"icon": "Cloud", "text": "Cloud Solutions"},
            {"icon": "Globe", "text": "Digital Marketing"}
        ],
        it_button1_text="IT Services",
        it_button1_link="/it",
        it_button2_text="Digital Services",
        it_button2_link="/digital",
        
        # Middle Hero Section
        hero_title="The Remote and Physical Business Consultancy With All Related IT Services",
        hero_subtitle="Professional consultancy to drive business growth and profitability",
        hero_features=[
            {"text": "Expert Consultants"},
            {"text": "Proven Solutions"},
            {"text": "24/7 Support"}
        ],
        
        is_active=True
    )
    
    print(f"✓ Created homepage content")
    return homepage

if __name__ == '__main__':
    print("Populating homepage content...")
    homepage = populate_homepage()
    print(f"\n✓ Homepage content populated successfully!")
    print(f"  - Accounting Title: {homepage.accounting_title}")
    print(f"  - IT Title: {homepage.it_title}")
    print(f"  - Hero Title: {homepage.hero_title}")
