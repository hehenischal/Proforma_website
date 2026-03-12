from core.models import Insight
from datetime import date

# Clear existing insights
Insight.objects.all().delete()

insights_data = [
    {
        "title": "Accounting Best Practices for Small Businesses",
        "slug": "accounting-best-practices",
        "excerpt": "Discover essential accounting practices that can help small businesses maintain financial health and compliance.",
        "introduction": "Maintaining proper accounting practices is crucial for the success of any small business. Proper financial management not only ensures compliance with regulations but also provides valuable insights for making informed business decisions.",
        "content_sections": [
            {
                "heading": "Separate Business and Personal Finances",
                "content": "One of the most fundamental practices is keeping your business and personal finances completely separate. This means having dedicated business bank accounts and credit cards.",
                "points": [
                    "Makes bookkeeping easier and more accurate",
                    "Simplifies tax preparation and filing",
                    "Provides legal protection for personal assets",
                    "Creates clear financial records for audits"
                ]
            },
            {
                "heading": "Implement a Reliable Bookkeeping System",
                "content": "Whether you choose cloud-based software or traditional methods, consistency is key. Modern accounting software can automate many tasks and provide real-time financial insights.",
                "points": [
                    "QuickBooks, Xero, or FreshBooks for automation",
                    "Real-time financial reporting and insights",
                    "Automated invoice generation and tracking",
                    "Integration with bank accounts and payment systems"
                ]
            },
            {
                "heading": "Track All Expenses",
                "content": "Every business expense should be documented and categorized. This includes receipts, invoices, and bank statements.",
                "points": [
                    "Ensures you don't miss tax deductions",
                    "Helps understand where money is going",
                    "Provides data for budgeting and forecasting",
                    "Required for audit compliance"
                ]
            },
            {
                "heading": "Regular Financial Reviews",
                "content": "Schedule monthly reviews of your financial statements including profit and loss statements, balance sheets, and cash flow statements.",
                "points": [
                    "Identify trends and patterns early",
                    "Spot problems before they become critical",
                    "Make informed strategic decisions",
                    "Track progress toward financial goals"
                ]
            }
        ],
        "conclusion": "Implementing these accounting best practices will help your small business maintain financial health, stay compliant with regulations, and make better business decisions. Consider working with a professional accountant to ensure you're following all relevant regulations and maximizing your financial efficiency.",
        "category": "Accounting",
        "author": "Samip Poudel",
        "read_time": "8 min read",
        "published_date": date(2024, 1, 15),
        "is_published": True,
        "is_featured": True
    },
    {
        "title": "Business Growth Strategies for 2024",
        "slug": "business-growth-strategies-2024",
        "excerpt": "Explore proven strategies to scale your business and achieve sustainable growth in the competitive market.",
        "introduction": "As we navigate through 2024, businesses need to adapt and implement effective growth strategies to stay competitive. Success requires a combination of innovation, strategic planning, and execution excellence.",
        "content_sections": [
            {
                "heading": "Digital Transformation",
                "content": "Embracing digital technologies is no longer optional. From cloud computing to AI-powered analytics, digital tools can streamline operations and improve customer experience.",
                "points": [
                    "Cloud computing for scalability and flexibility",
                    "AI-powered analytics for data-driven decisions",
                    "Automation to improve efficiency",
                    "Digital marketing to reach wider audiences"
                ]
            },
            {
                "heading": "Customer-Centric Approach",
                "content": "Understanding and meeting customer needs should be at the heart of your growth strategy. Use data analytics to gain insights into customer behavior and preferences.",
                "points": [
                    "Personalize offerings and communications",
                    "Build stronger customer relationships",
                    "Improve customer retention rates",
                    "Increase customer lifetime value"
                ]
            },
            {
                "heading": "Strategic Partnerships",
                "content": "Collaborate with complementary businesses to expand your reach and capabilities. Strategic partnerships can help you access new markets and share resources.",
                "points": [
                    "Access to new markets and customers",
                    "Shared resources and expertise",
                    "Innovation through collaboration",
                    "Risk mitigation through diversification"
                ]
            },
            {
                "heading": "Invest in Your Team",
                "content": "Your employees are your greatest asset. Invest in training and development programs to enhance their skills and create a positive work culture.",
                "points": [
                    "Enhanced employee skills and productivity",
                    "Improved employee retention",
                    "Stronger company culture",
                    "Better customer service delivery"
                ]
            }
        ],
        "conclusion": "Sustainable business growth requires a combination of strategic planning, innovation, and execution. By implementing these strategies and remaining adaptable to market changes, your business can achieve long-term success in 2024 and beyond.",
        "category": "Business",
        "author": "Rajesh Sharma",
        "read_time": "10 min read",
        "published_date": date(2024, 2, 1),
        "is_published": True,
        "is_featured": True
    },
    {
        "title": "Understanding Tax Planning in Nepal",
        "slug": "tax-planning-nepal",
        "excerpt": "A comprehensive guide to tax planning strategies for individuals and businesses in Nepal.",
        "introduction": "Tax planning is an essential aspect of financial management for both individuals and businesses in Nepal. Understanding the tax system and implementing effective strategies can help you minimize tax liability while remaining compliant with regulations.",
        "content_sections": [
            {
                "heading": "Nepal's Tax System Overview",
                "content": "Nepal operates a progressive tax system with various types of taxes. The Inland Revenue Department (IRD) is responsible for tax administration.",
                "points": [
                    "Income tax on personal and business income",
                    "Value-added tax (VAT) on goods and services",
                    "Excise duty on specific products",
                    "Customs duty on imports"
                ]
            },
            {
                "heading": "Key Tax Planning Strategies",
                "content": "Effective tax planning requires understanding available deductions and strategic timing of income and expenses.",
                "points": [
                    "Maximize allowable deductions and exemptions",
                    "Strategic timing of income and expenses",
                    "Investment in tax-advantaged schemes",
                    "Proper business structure selection"
                ]
            },
            {
                "heading": "Common Tax Deductions",
                "content": "Familiarize yourself with allowable deductions that can significantly reduce your taxable income.",
                "points": [
                    "Retirement fund contributions",
                    "Life and health insurance premiums",
                    "Charitable donations to approved organizations",
                    "Medical expenses within limits"
                ]
            },
            {
                "heading": "Compliance Requirements",
                "content": "Staying compliant with tax regulations is crucial to avoid penalties and maintain good standing with tax authorities.",
                "points": [
                    "Timely filing of tax returns",
                    "Accurate record keeping for 7 years",
                    "Regular advance tax payments",
                    "Proper documentation of all transactions"
                ]
            }
        ],
        "conclusion": "Effective tax planning requires ongoing attention and professional guidance. Consider working with a qualified tax consultant to develop a comprehensive strategy tailored to your specific situation. Remember, tax planning is about legal optimization, not evasion.",
        "category": "Tax",
        "author": "Priya Thapa",
        "read_time": "7 min read",
        "published_date": date(2024, 1, 20),
        "is_published": True,
        "is_featured": False
    },
    {
        "title": "Digital Transformation: A Guide for Nepali Businesses",
        "slug": "digital-transformation-guide",
        "excerpt": "Learn how digital transformation can revolutionize your business operations and customer experience.",
        "introduction": "Digital transformation is reshaping the business landscape in Nepal. Companies that embrace digital technologies are gaining competitive advantages, improving efficiency, and delivering better customer experiences. This guide will help you understand and implement digital transformation in your business.",
        "content_sections": [
            {
                "heading": "What is Digital Transformation",
                "content": "Digital transformation involves integrating digital technology into all areas of business, fundamentally changing how you operate and deliver value to customers.",
                "points": [
                    "Reimagining business processes with technology",
                    "Improving operational efficiency",
                    "Enhancing customer experience",
                    "Creating new revenue streams"
                ]
            },
            {
                "heading": "Key Areas of Digital Transformation",
                "content": "Focus on these critical areas to maximize the impact of your digital transformation efforts.",
                "points": [
                    "Cloud computing for flexibility and scalability",
                    "Customer Relationship Management (CRM) systems",
                    "E-commerce and digital payment solutions",
                    "Data analytics for informed decision-making"
                ]
            },
            {
                "heading": "Steps to Begin Your Journey",
                "content": "Start your digital transformation with a strategic approach to ensure success and minimize risks.",
                "points": [
                    "Assess your current technology and processes",
                    "Define clear, measurable objectives",
                    "Start with pilot projects in specific areas",
                    "Invest in employee training and development"
                ]
            },
            {
                "heading": "Overcoming Common Challenges",
                "content": "Address these common challenges to ensure smooth digital transformation implementation.",
                "points": [
                    "Manage resistance to change through communication",
                    "Start with cost-effective solutions",
                    "Bridge skill gaps with training programs",
                    "Plan integration carefully for compatibility"
                ]
            }
        ],
        "conclusion": "Digital transformation is a journey, not a destination. By taking a strategic approach and remaining committed to continuous improvement, Nepali businesses can leverage technology to achieve sustainable growth and competitive advantage in the digital age.",
        "category": "Technology",
        "author": "Anil Kumar",
        "read_time": "9 min read",
        "published_date": date(2024, 2, 5),
        "is_published": True,
        "is_featured": True
    }
]

print("Creating structured insights...")
for insight_data in insights_data:
    insight = Insight.objects.create(**insight_data)
    print(f"✅ Created: {insight.title}")
    print(f"   - Sections: {len(insight.content_sections)}")

print(f"\n✅ Total insights created: {Insight.objects.count()}")
print(f"✅ Published insights: {Insight.objects.filter(is_published=True).count()}")
print(f"✅ Featured insights: {Insight.objects.filter(is_featured=True).count()}")
