from core.models import CompanyInfo

# Delete existing company info if any
CompanyInfo.objects.all().delete()

# Create company info with About page content
company_info = CompanyInfo.objects.create(
    company_name="Proforma Insights",
    tagline="Your Trusted Partner for Business Consultancy & IT Solutions",
    about_text="Proforma Insights is committed to helping businesses thrive in today's competitive landscape by providing remote and physical business consultancy services with cutting-edge IT solutions integrated at every level.",
    
    # About Page Hero
    hero_title="Leading Business Consultant in Nepal",
    hero_subtitle="Proforma Insights is Nepal's premier business & IT consultancy, offering expert tax planning, accounting, compliance, and strategic consulting services with precision and dedication.",
    
    # History Section
    history_title="Our Journey",
    history_text="Founded in 2010, Proforma Insights has evolved from a small consultancy to a trusted leader in Nepal's business landscape. Over the years, we have continuously expanded our expertise and service portfolio to meet the evolving needs of our clients, helping them navigate complex business challenges and achieve sustainable growth.",
    
    # Core Values
    values=[
        {
            "icon_name": "Award",
            "title": "Excellence",
            "description": "Commitment to delivering exceptional quality in every service"
        },
        {
            "icon_name": "Users",
            "title": "Collaboration",
            "description": "Building strong partnerships with our clients"
        },
        {
            "icon_name": "Clock",
            "title": "Reliability",
            "description": "Consistent and dependable service delivery"
        },
        {
            "icon_name": "Target",
            "title": "Innovation",
            "description": "Embracing new technologies and approaches"
        }
    ],
    
    # Key Benefits
    benefits=[
        "Deep understanding of the Nepali business environment",
        "Experienced team of certified professionals",
        "Personalized solutions tailored to client needs",
        "Comprehensive service offerings under one roof",
        "Proven track record of client success",
        "Continuous support and guidance",
        "Proactive compliance management and risk mitigation",
        "Advanced technology integration for operations",
        "Transparent communication and regular updates",
        "Commitment to long-term partnerships",
        "Focus on sustainable growth and success"
    ],
    
    # Contact Information
    address="Pokhara-07, RatnaChowk",
    city="Pokhara",
    country="Nepal",
    phone="+977 061-545445",
    email="info@proformainsights.com",
    working_hours="Sun - Fri: 9:00 AM - 6:00 PM",
    
    # Social Media
    facebook_url="https://facebook.com/proformainsights",
    instagram_url="https://instagram.com/proformainsights",
    linkedin_url="https://linkedin.com/company/proformainsights",
    youtube_url="https://youtube.com/@proformainsights",
)

print("✅ Company Information created successfully!")
print(f"Company Name: {company_info.company_name}")
print(f"Values: {len(company_info.values)} items")
print(f"Benefits: {len(company_info.benefits)} items")
