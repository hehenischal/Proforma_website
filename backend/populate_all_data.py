"""
Comprehensive script to populate all database models with initial data
Run with: python manage.py shell < populate_all_data.py
Or: Get-Content populate_all_data.py | python manage.py shell
"""

from core.models import (
    Service, TeamMember, Insight, SliderImage,
    CompanyStat, CompanyInfo
)
from datetime import date

print("=" * 60)
print("POPULATING DATABASE WITH INITIAL DATA")
print("=" * 60)

# ============================================================================
# 1. SERVICES
# ============================================================================
print("\n1. Adding Services...")

services_data = [
    {
        "title": "Accounting Services",
        "slug": "accounting",
        "icon_name": "Calculator",
        "short_description": "Professional accounting services tailored to your business needs",
        "full_description": "Comprehensive accounting solutions including bookkeeping, financial reporting, budgeting, and financial analysis. We help businesses maintain accurate financial records and make informed decisions.",
        "features": [
            "Bookkeeping & Financial Reporting",
            "Budgeting & Forecasting",
            "Financial Statement Analysis",
            "Payroll Processing",
            "Compliance Management"
        ],
        "order": 1,
        "is_active": True
    },
    {
        "title": "Tax Services",
        "slug": "tax",
        "icon_name": "FileText",
        "short_description": "Expert tax planning and compliance solutions",
        "full_description": "Professional tax consulting services to minimize liabilities and ensure compliance. We provide strategic tax planning, preparation, and audit support for individuals and businesses.",
        "features": [
            "Tax Planning & Strategy",
            "Tax Return Preparation",
            "Compliance Management",
            "Tax Audit Support",
            "International Tax Services"
        ],
        "order": 2,
        "is_active": True
    },
    {
        "title": "IT Solutions",
        "slug": "it",
        "icon_name": "Monitor",
        "short_description": "Comprehensive IT solutions for modern businesses",
        "full_description": "End-to-end IT services including software development, cloud solutions, cybersecurity, and infrastructure management. We help businesses leverage technology for growth.",
        "features": [
            "Software Development",
            "Cloud Solutions & Migration",
            "IT Infrastructure Management",
            "Cybersecurity Services",
            "Digital Transformation"
        ],
        "order": 3,
        "is_active": True
    },
    {
        "title": "Digital Marketing",
        "slug": "digital",
        "icon_name": "TrendingUp",
        "short_description": "Innovative digital transformation strategies",
        "full_description": "Strategic digital marketing services to enhance your online presence. We offer SEO, social media marketing, content strategy, and brand development to help you reach your target audience.",
        "features": [
            "SEO & SEM Strategy",
            "Social Media Marketing",
            "Content Marketing",
            "Brand Development",
            "Marketing Analytics"
        ],
        "order": 4,
        "is_active": True
    }
]

for service_data in services_data:
    service, created = Service.objects.update_or_create(
        slug=service_data['slug'],
        defaults=service_data
    )
    print(f"  {'Created' if created else 'Updated'}: {service.title}")

print(f"  Total services: {Service.objects.filter(is_active=True).count()}")

# ============================================================================
# 2. TEAM MEMBERS
# ============================================================================
print("\n2. Adding Team Members...")

team_data = [
    {
        "name": "Binod Pokhrel",
        "position": "Founder & CEO",
        "bio": "Binod Pokhrel is the visionary behind Proforma Insights, leading the company with a passion for innovation and excellence in business consultancy.",
        "email": "proformaconsultant@gmail.com",
        "phone": "+977-984-XXXXXXX",
        "order": 1,
        "is_active": True
    },
    {
        "name": "Janak Subedi",
        "position": "Chartered Accountant",
        "bio": "Janak Subedi is a seasoned Chartered Accountant with expertise in financial management and strategic planning, ensuring our clients achieve their business goals.",
        "email": "proformaconsultant@gmail.com",
        "phone": "+977-984-XXXXXXX",
        "order": 2,
        "is_active": True
    },
    {
        "name": "Samit Paudel",
        "position": "IT Officer",
        "bio": "Samit Paudel manages our IT infrastructure and ensures seamless operations across all departments with cutting-edge technology solutions.",
        "email": "proformadigitaltech@gmail.com",
        "phone": "+977-984-XXXXXXX",
        "order": 3,
        "is_active": True
    },
    {
        "name": "Suraj Pandey",
        "position": "Chief Technology Officer",
        "bio": "Suraj Pandey develops and maintains our web applications, ensuring they are robust, scalable, and user-friendly with modern tech stacks.",
        "email": "proformadigitaltech@gmail.com",
        "phone": "+977-984-XXXXXXX",
        "order": 4,
        "is_active": True
    },
    {
        "name": "Soonam Chaudary",
        "position": "Finance Officer",
        "bio": "Soonam handles our financial accounting with precision and ensures compliance with all regulatory requirements and standards.",
        "email": "proformaconsultant@gmail.com",
        "phone": "+977-984-XXXXXXX",
        "order": 5,
        "is_active": True
    },
    {
        "name": "Samip Baral",
        "position": "Frontend Intern",
        "bio": "Samip Baral is a frontend intern at Proforma Insights, contributing to various projects and learning from experienced professionals.",
        "email": "samipbaral.proforma@gmail.com",
        "phone": "+977-984-XXXXXXX",
        "order": 6,
        "is_active": True
    }
]

for member_data in team_data:
    member, created = TeamMember.objects.update_or_create(
        name=member_data['name'],
        defaults=member_data
    )
    print(f"  {'Created' if created else 'Updated'}: {member.name}")

print(f"  Total team members: {TeamMember.objects.filter(is_active=True).count()}")

# ============================================================================
# 3. COMPANY STATISTICS
# ============================================================================
print("\n3. Adding Company Statistics...")

stats_data = [
    {
        "label": "Happy Clients",
        "value": 100,
        "suffix": "+",
        "icon_name": "Users",
        "order": 1,
        "is_active": True
    },
    {
        "label": "Projects Completed",
        "value": 100,
        "suffix": "+",
        "icon_name": "Briefcase",
        "order": 2,
        "is_active": True
    },
    {
        "label": "Years Experience",
        "value": 5,
        "suffix": "+",
        "icon_name": "Award",
        "order": 3,
        "is_active": True
    },
    {
        "label": "Team Members",
        "value": 10,
        "suffix": "+",
        "icon_name": "Users",
        "order": 4,
        "is_active": True
    }
]

for stat_data in stats_data:
    stat, created = CompanyStat.objects.update_or_create(
        label=stat_data['label'],
        defaults=stat_data
    )
    print(f"  {'Created' if created else 'Updated'}: {stat.label}")

print(f"  Total stats: {CompanyStat.objects.filter(is_active=True).count()}")

# ============================================================================
# 4. COMPANY INFO
# ============================================================================
print("\n4. Adding Company Information...")

company_info_data = {
    "company_name": "Proforma Insights",
    "tagline": "Your Trusted Business Partner",
    "about_text": "Proforma Insights is Nepal's premier business & IT consultancy, offering expert tax planning, accounting, compliance, and strategic consulting services with precision and dedication.",
    "address": "Ratnachowk, Pokhara",
    "city": "Pokhara",
    "country": "Nepal",
    "phone": "+977-61-545445",
    "email": "proformadigitaltech@gmail.com",
    "working_hours": "Sunday - Friday: 9:00 AM - 5:00 PM",
    "facebook_url": "https://www.facebook.com/profile.php?id=61586117833991",
    "instagram_url": "https://www.instagram.com/proformainsights/",
    "linkedin_url": "https://www.linkedin.com/company/proforma-insight/",
    "youtube_url": "",
    "google_maps_embed": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1580.5994759576663!2d83.97558819161135!3d28.204317256884618!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39959549cdd845fd%3A0x42037efae8914320!2sGandaki%20Province%20Academy%20of%20Science%20and%20Technology%20(GPAST)%20(Administration%20office)!5e0!3m2!1sen!2snp!4v1769156164126!5m2!1sen!2snp"
}

# Company info is singleton, so we update or create the first instance
if CompanyInfo.objects.exists():
    company_info = CompanyInfo.objects.first()
    for key, value in company_info_data.items():
        setattr(company_info, key, value)
    company_info.save()
    print(f"  Updated: {company_info.company_name}")
else:
    company_info = CompanyInfo.objects.create(**company_info_data)
    print(f"  Created: {company_info.company_name}")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "=" * 60)
print("DATABASE POPULATION COMPLETE!")
print("=" * 60)
print(f"Services: {Service.objects.filter(is_active=True).count()}")
print(f"Team Members: {TeamMember.objects.filter(is_active=True).count()}")
print(f"Statistics: {CompanyStat.objects.filter(is_active=True).count()}")
print(f"Company Info: {'Yes' if CompanyInfo.objects.exists() else 'No'}")
print(f"Insights: {Insight.objects.filter(is_published=True).count()}")
print(f"Slider Images: {SliderImage.objects.filter(is_active=True).count()}")
print("=" * 60)
print("\nNote: Add Insights and Slider Images via admin panel")
print("Admin: http://localhost:8000/admin/")
print("=" * 60)
