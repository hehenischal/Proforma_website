from core.models import Insight
from datetime import date

# Clear existing insights
Insight.objects.all().delete()

insights_data = [
    {
        "title": "Business Growth Strategies for 2024",
        "slug": "business-growth-strategies-2024",
        "excerpt": "Explore proven strategies to scale your business and achieve sustainable growth in the competitive market.",
        "content_blocks": [
            {
                "type": "paragraph",
                "content": "As we navigate through 2024, businesses need to adapt and implement effective growth strategies to stay competitive. Success requires a combination of innovation, strategic planning, and execution excellence."
            },
            {
                "type": "heading",
                "content": "Digital Transformation"
            },
            {
                "type": "paragraph",
                "content": "Embracing digital technologies is no longer optional. From cloud computing to AI-powered analytics, digital tools can streamline operations and improve customer experience."
            },
            {
                "type": "list",
                "content": [
                    "Cloud computing for scalability and flexibility",
                    "AI-powered analytics for data-driven decisions",
                    "Automation to improve efficiency",
                    "Digital marketing to reach wider audiences"
                ]
            },
            {
                "type": "heading",
                "content": "Customer-Centric Approach"
            },
            {
                "type": "paragraph",
                "content": "Understanding and meeting customer needs should be at the heart of your growth strategy. Use data analytics to gain insights into customer behavior and preferences."
            },
            {
                "type": "list",
                "content": [
                    "Personalize offerings and communications",
                    "Build stronger customer relationships",
                    "Improve customer retention rates",
                    "Increase customer lifetime value"
                ]
            },
            {
                "type": "heading",
                "content": "Strategic Partnerships"
            },
            {
                "type": "paragraph",
                "content": "Collaborate with complementary businesses to expand your reach and capabilities. Strategic partnerships can help you access new markets and share resources."
            },
            {
                "type": "list",
                "content": [
                    "Access to new markets and customers",
                    "Shared resources and expertise",
                    "Innovation through collaboration",
                    "Risk mitigation through diversification"
                ]
            },
            {
                "type": "heading",
                "content": "Final Thoughts"
            },
            {
                "type": "paragraph",
                "content": "Sustainable business growth requires a combination of strategic planning, innovation, and execution. By implementing these strategies and remaining adaptable to market changes, your business can achieve long-term success in 2024 and beyond."
            }
        ],
        "category": "Business",
        "author": "Rajesh Sharma",
        "read_time": "10 min read",
        "published_date": date(2024, 2, 1),
        "is_published": True,
        "is_featured": True
    },
    {
        "title": "Accounting Best Practices for Small Businesses",
        "slug": "accounting-best-practices",
        "excerpt": "Discover essential accounting practices that can help small businesses maintain financial health and compliance.",
        "content_blocks": [
            {
                "type": "paragraph",
                "content": "Maintaining proper accounting practices is crucial for the success of any small business. Proper financial management not only ensures compliance with regulations but also provides valuable insights for making informed business decisions."
            },
            {
                "type": "heading",
                "content": "Separate Business and Personal Finances"
            },
            {
                "type": "paragraph",
                "content": "One of the most fundamental practices is keeping your business and personal finances completely separate. This means having dedicated business bank accounts and credit cards."
            },
            {
                "type": "list",
                "content": [
                    "Makes bookkeeping easier and more accurate",
                    "Simplifies tax preparation and filing",
                    "Provides legal protection for personal assets",
                    "Creates clear financial records for audits"
                ]
            },
            {
                "type": "heading",
                "content": "Implement a Reliable Bookkeeping System"
            },
            {
                "type": "paragraph",
                "content": "Whether you choose cloud-based software or traditional methods, consistency is key. Modern accounting software can automate many tasks and provide real-time financial insights."
            },
            {
                "type": "list",
                "content": [
                    "QuickBooks, Xero, or FreshBooks for automation",
                    "Real-time financial reporting and insights",
                    "Automated invoice generation and tracking",
                    "Integration with bank accounts and payment systems"
                ]
            },
            {
                "type": "heading",
                "content": "Conclusion"
            },
            {
                "type": "paragraph",
                "content": "Implementing these accounting best practices will help your small business maintain financial health, stay compliant with regulations, and make better business decisions. Consider working with a professional accountant to ensure you're following all relevant regulations."
            }
        ],
        "category": "Accounting",
        "author": "Samip Poudel",
        "read_time": "8 min read",
        "published_date": date(2024, 1, 15),
        "is_published": True,
        "is_featured": True
    }
]

print("Creating insights with flexible content blocks...")
for insight_data in insights_data:
    insight = Insight.objects.create(**insight_data)
    print(f"✅ Created: {insight.title}")
    print(f"   - Content blocks: {len(insight.content_blocks)}")

print(f"\n✅ Total insights created: {Insight.objects.count()}")
print(f"✅ Published insights: {Insight.objects.filter(is_published=True).count()}")
print(f"✅ Featured insights: {Insight.objects.filter(is_featured=True).count()}")

print("\n📝 Content blocks format:")
print("   - paragraph: Regular text")
print("   - heading: Section title")
print("   - list: Bullet points with checkmarks")
