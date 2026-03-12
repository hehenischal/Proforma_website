import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proforma_backend.settings')
django.setup()

from core.models import Service

def populate_services():
    """Populate services with detailed content for both cards and detail pages"""
    
    services_data = [
        {
            'title': 'Accounting Services',
            'slug': 'accounting',
            'icon_name': 'Calculator',
            'color': '#0066cc',
            'short_description': 'Professional accounting services tailored to your business needs',
            'features': [
                'Bookkeeping & Financial Reporting',
                'Budgeting & Forecasting',
                'Financial Statement Analysis',
                'Payroll Processing',
                'Compliance Management'
            ],
            'hero_title': 'Accounting Services',
            'hero_subtitle': 'Professional accounting solutions to keep your business financially healthy',
            'full_description': 'Our comprehensive accounting services ensure your business maintains accurate financial records and stays compliant with all regulations.',
            'detail_content': 'We provide end-to-end accounting solutions that combine strategic insight with practical implementation. Our team of experienced accountants works closely with you to understand your business needs and deliver customized solutions.',
            'services_list': [
                'Bookkeeping & Financial Reporting',
                'Budgeting & Forecasting',
                'Financial Statement Analysis',
                'Payroll Processing',
                'Compliance Management',
                'Tax Planning & Preparation'
            ],
            'order': 1
        },
        {
            'title': 'Tax Services',
            'slug': 'tax',
            'icon_name': 'FileText',
            'color': '#0066cc',
            'short_description': 'Expert tax planning and compliance solutions',
            'features': [
                'Tax Planning & Strategy',
                'Tax Return Preparation',
                'Compliance Management',
                'Tax Audit Support',
                'International Tax Services'
            ],
            'hero_title': 'Tax Services',
            'hero_subtitle': 'Strategic tax planning and compliance solutions for your business',
            'full_description': 'Navigate complex tax regulations with confidence through our expert tax services designed to minimize your tax liability while ensuring full compliance.',
            'detail_content': 'Our tax professionals stay up-to-date with the latest tax laws and regulations to provide you with accurate, timely tax services. We help you make informed decisions that optimize your tax position.',
            'services_list': [
                'Tax Planning & Strategy',
                'Tax Return Preparation',
                'Compliance Management',
                'Tax Audit Support',
                'International Tax Services',
                'Tax Advisory Services'
            ],
            'order': 2
        },
        {
            'title': 'IT Solutions',
            'slug': 'it',
            'icon_name': 'Cpu',
            'color': '#0066cc',
            'short_description': 'Comprehensive IT solutions for modern businesses',
            'features': [
                'Software Development',
                'Cloud Solutions & Migration',
                'IT Infrastructure Management',
                'Cybersecurity Services',
                'Digital Transformation'
            ],
            'hero_title': 'IT Solutions',
            'hero_subtitle': 'Innovative technology solutions to transform your business operations',
            'full_description': 'Leverage cutting-edge technology to streamline operations, enhance productivity, and drive business growth with our comprehensive IT solutions.',
            'detail_content': 'From custom software development to cloud migration and cybersecurity, we provide end-to-end IT services that help your business stay competitive in the digital age.',
            'services_list': [
                'Software Development',
                'Cloud Solutions & Migration',
                'IT Infrastructure Management',
                'Cybersecurity Services',
                'Digital Transformation',
                'IT Consulting & Strategy'
            ],
            'order': 3
        },
        {
            'title': 'Digital Marketing',
            'slug': 'digital',
            'icon_name': 'TrendingUp',
            'color': '#0066cc',
            'short_description': 'Innovative digital transformation strategies',
            'features': [
                'SEO & SEM Strategy',
                'Social Media Marketing',
                'Content Marketing',
                'Brand Development',
                'Marketing Analytics'
            ],
            'hero_title': 'Digital Marketing',
            'hero_subtitle': 'Data-driven digital marketing strategies to grow your business',
            'full_description': 'Reach your target audience and drive measurable results with our comprehensive digital marketing services tailored to your business goals.',
            'detail_content': 'Our digital marketing experts combine creativity with data-driven strategies to help you build brand awareness, generate leads, and increase conversions across all digital channels.',
            'services_list': [
                'SEO & SEM Strategy',
                'Social Media Marketing',
                'Content Marketing',
                'Brand Development',
                'Marketing Analytics',
                'Email Marketing Campaigns'
            ],
            'order': 4
        },
        {
            'title': 'Business Consulting',
            'slug': 'business-consulting',
            'icon_name': 'Briefcase',
            'color': '#0066cc',
            'short_description': 'Expert business consulting for growth',
            'features': [
                'Strategy Development',
                'Business Planning',
                'Process Optimization',
                'Change Management',
                'Performance Improvement'
            ],
            'hero_title': 'Business Consulting',
            'hero_subtitle': 'Strategic consulting services to drive sustainable business growth',
            'full_description': 'Partner with our experienced consultants to develop and implement strategies that drive sustainable growth and operational excellence.',
            'detail_content': 'We work closely with your team to understand your unique challenges and opportunities, delivering actionable insights and practical solutions that create lasting value.',
            'services_list': [
                'Strategy Development',
                'Business Planning',
                'Process Optimization',
                'Change Management',
                'Performance Improvement',
                'Market Analysis'
            ],
            'order': 5
        }
    ]
    
    for service_data in services_data:
        service, created = Service.objects.update_or_create(
            slug=service_data['slug'],
            defaults=service_data
        )
        
        if created:
            print(f"✓ Created service: {service.title}")
        else:
            print(f"✓ Updated service: {service.title}")
    
    print(f"\n✓ Successfully populated {len(services_data)} services with detailed content!")
    print("\nYou can now:")
    print("1. Go to Django admin to edit service content")
    print("2. Add images for cards and detail pages")
    print("3. Customize the content for each service")

if __name__ == '__main__':
    populate_services()
