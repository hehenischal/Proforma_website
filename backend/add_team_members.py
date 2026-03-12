"""
Script to add team members to the database
Run with: python manage.py shell < add_team_members.py
"""

from core.models import TeamMember

# Clear existing team members (optional)
# TeamMember.objects.all().delete()

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

# Add team members
for member_data in team_data:
    # Check if member already exists
    existing = TeamMember.objects.filter(name=member_data['name']).first()
    if existing:
        print(f"Updating: {member_data['name']}")
        for key, value in member_data.items():
            setattr(existing, key, value)
        existing.save()
    else:
        print(f"Creating: {member_data['name']}")
        TeamMember.objects.create(**member_data)

print(f"\nTotal active team members: {TeamMember.objects.filter(is_active=True).count()}")
print("Team members added successfully!")
