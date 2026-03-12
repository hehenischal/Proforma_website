import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proforma_backend.settings')
django.setup()

from core.models import Project

def populate_projects():
    """Populate sample projects"""
    
    # Delete existing data
    Project.objects.all().delete()
    
    projects_data = [
        {
            'title': 'E-Commerce Platform Development',
            'description': 'Built a comprehensive e-commerce platform with payment integration, inventory management, and customer analytics for a retail client.',
            'category': 'Web Development',
            'client_name': 'Retail Solutions Inc.',
            'project_date': date(2024, 1, 15),
            'technologies': ['React', 'Node.js', 'MongoDB', 'Stripe'],
            'project_url': 'https://example-ecommerce.com',
            'order': 1,
            'is_featured': True,
            'is_active': True,
        },
        {
            'title': 'Financial Management System',
            'description': 'Developed a custom financial management and accounting system with automated reporting and tax calculation features.',
            'category': 'Accounting Software',
            'client_name': 'Finance Corp',
            'project_date': date(2024, 2, 20),
            'technologies': ['Python', 'Django', 'PostgreSQL'],
            'project_url': 'https://example-finance.com',
            'order': 2,
            'is_featured': True,
            'is_active': True,
        },
        {
            'title': 'Cloud Infrastructure Migration',
            'description': 'Successfully migrated client infrastructure to AWS cloud with improved scalability, security, and cost optimization.',
            'category': 'IT Solutions',
            'client_name': 'Tech Innovations Ltd.',
            'project_date': date(2023, 11, 10),
            'technologies': ['AWS', 'Docker', 'Kubernetes', 'Terraform'],
            'project_url': 'https://example-cloud.com',
            'order': 3,
            'is_featured': True,
            'is_active': True,
        },
        {
            'title': 'Digital Marketing Campaign',
            'description': 'Executed a comprehensive digital marketing campaign including SEO, social media, and content marketing strategies.',
            'category': 'Digital Marketing',
            'client_name': 'Brand Builders',
            'project_date': date(2024, 3, 5),
            'technologies': ['Google Ads', 'Facebook Ads', 'SEO Tools'],
            'project_url': 'https://example-marketing.com',
            'order': 4,
            'is_featured': True,
            'is_active': True,
        },
        {
            'title': 'Mobile App Development',
            'description': 'Created a cross-platform mobile application for business management with real-time synchronization and offline capabilities.',
            'category': 'Mobile Development',
            'client_name': 'Business Solutions Co.',
            'project_date': date(2023, 12, 15),
            'technologies': ['React Native', 'Firebase', 'Redux'],
            'project_url': 'https://example-mobile.com',
            'order': 5,
            'is_featured': True,
            'is_active': True,
        },
        {
            'title': 'Tax Compliance Automation',
            'description': 'Implemented automated tax compliance system with real-time calculations and regulatory updates for multiple jurisdictions.',
            'category': 'Tax Services',
            'client_name': 'Global Enterprises',
            'project_date': date(2024, 1, 30),
            'technologies': ['Python', 'API Integration', 'Machine Learning'],
            'project_url': 'https://example-tax.com',
            'order': 6,
            'is_featured': True,
            'is_active': True,
        },
    ]
    
    created_projects = []
    for project_data in projects_data:
        project = Project.objects.create(**project_data)
        created_projects.append(project)
        print(f"✓ Created project: {project.title}")
    
    return created_projects

if __name__ == '__main__':
    print("Populating projects...")
    projects = populate_projects()
    print(f"\n✓ Successfully created {len(projects)} projects!")
    print("\nNote: Please add images manually through the Django admin panel at:")
    print("http://localhost:8000/admin/core/project/")
