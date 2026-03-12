from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    """Service offerings like Accounting, Tax, IT, Digital"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    icon_name = models.CharField(max_length=50, help_text="Lucide icon name (e.g., Calculator, FileText)")
    color = models.CharField(max_length=7, default='#0066cc', help_text="Hex color code for the service")
    short_description = models.TextField()
    full_description = models.TextField()
    
    # Detail page fields
    hero_title = models.CharField(max_length=200, blank=True, help_text="Title for detail page hero section")
    hero_subtitle = models.TextField(blank=True, help_text="Subtitle for detail page hero section")
    detail_content = models.TextField(blank=True, help_text="Main content for detail page")
    services_list = models.JSONField(default=list, help_text="List of specific services offered")
    
    # Images
    image = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Card image")
    detail_image = models.ImageField(upload_to='services/', blank=True, null=True, help_text="Detail page image")
    
    features = models.JSONField(default=list, help_text="List of key features")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class TeamMember(models.Model):
    """Team members information"""
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    linkedin = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.position}"


class Insight(models.Model):
    """Blog posts/insights"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField()
    
    # Flexible content structure
    content_blocks = models.JSONField(
        default=list,
        help_text='Content blocks with type and content. Types: paragraph, heading, list'
    )
    
    # Legacy fields (kept for backward compatibility)
    introduction = models.TextField(blank=True, help_text="Legacy: Opening paragraph")
    content_sections = models.JSONField(default=list, blank=True, help_text="Legacy: Structured sections")
    conclusion = models.TextField(blank=True, help_text="Legacy: Closing paragraph")
    content = models.TextField(blank=True, help_text="Legacy: Full content field")
    
    image = models.ImageField(upload_to='insights/', blank=True, null=True)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="Proforma Team")
    read_time = models.CharField(max_length=20, default="5 min read")
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class SliderImage(models.Model):
    """Homepage slider images"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='slider/')
    button_text = models.CharField(max_length=50, blank=True)
    button_link = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class CompanyStat(models.Model):
    """Company statistics for counter section"""
    label = models.CharField(max_length=100)
    value = models.IntegerField()
    suffix = models.CharField(max_length=10, blank=True, help_text="e.g., +, %, K")
    icon_name = models.CharField(max_length=50, help_text="Lucide icon name")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = "Company Statistic"
        verbose_name_plural = "Company Statistics"

    def __str__(self):
        return f"{self.label}: {self.value}{self.suffix}"


class ContactInquiry(models.Model):
    """Contact form submissions"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    is_responded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Inquiry"
        verbose_name_plural = "Contact Inquiries"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"


class ProformaCard(models.Model):
    """Dynamic cards for More About Proforma section (Vision, Mission, Benefits, etc.)"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    icon_name = models.CharField(max_length=50, help_text="Lucide icon name (e.g., Crosshair, Star, Rocket)")
    
    # Flexible content structure using ContentBlocksWidget
    content_blocks = models.JSONField(
        default=list,
        help_text='Content blocks with type and content. Types: paragraph, heading, list'
    )
    
    image = models.ImageField(upload_to='proforma_cards/', blank=True, null=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Proforma Card"
        verbose_name_plural = "Proforma Cards"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class CompanyInfo(models.Model):
    """Company information (singleton)"""
    company_name = models.CharField(max_length=200, default="Proforma Insights")
    tagline = models.CharField(max_length=300)
    about_text = models.TextField()
    
    # About Page Content
    hero_title = models.CharField(max_length=300, default="Leading Business Consultant in Nepal")
    hero_subtitle = models.TextField(default="Proforma Insights is Nepal's premier business & IT consultancy")
    history_title = models.CharField(max_length=200, default="Our Journey")
    history_text = models.TextField(blank=True)
    values = models.JSONField(default=list, help_text="List of company values with title and description")
    benefits = models.JSONField(default=list, help_text="List of key benefits/advantages")
    
    # Contact Information
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    working_hours = models.CharField(max_length=100)
    
    # Social Media
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    
    # Other
    google_maps_embed = models.TextField(blank=True)
    logo = models.ImageField(upload_to='company/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and CompanyInfo.objects.exists():
            raise ValueError('Only one CompanyInfo instance is allowed')
        super().save(*args, **kwargs)


class CoreValue(models.Model):
    """Core values displayed on About page"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_name = models.CharField(
        max_length=50, 
        help_text="Lucide icon name. Suggestions: Award (Excellence), Target (Goals), Users (Teamwork), Shield (Integrity), Heart (Care), Lightbulb (Innovation), TrendingUp (Growth), CheckCircle (Quality), Handshake (Trust), Zap (Efficiency)"
    )
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Core Value"
        verbose_name_plural = "Core Values"

    def __str__(self):
        return self.title


class WorkEnvironmentImage(models.Model):
    """Work environment gallery images for About page"""
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='work_environment/')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Work Environment Image"
        verbose_name_plural = "Work Environment Images"

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    """Why Choose Us section content (singleton)"""
    # Key Advantages List
    key_advantages = models.JSONField(
        default=list,
        help_text="List of key advantages/benefits (e.g., ['Deep understanding of Nepali business', 'Experienced team'])"
    )
    
    # Trusted Partner Section
    partner_title = models.CharField(max_length=200, default="Your Trusted Partner")
    partner_description = models.TextField(
        help_text="Main paragraph describing why clients should choose you"
    )
    
    # Numbered Points (Dynamic List)
    numbered_points = models.JSONField(
        default=list,
        help_text='List of numbered points with title and description. Example: [{"title": "Expert Guidance", "description": "Professional advice from experienced consultants"}, {"title": "Innovative Solutions", "description": "Cutting-edge approaches"}]'
    )
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Why Choose Us Content"
        verbose_name_plural = "Why Choose Us Content"

    def __str__(self):
        return "Why Choose Us Section"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and WhyChooseUs.objects.exists():
            raise ValueError('Only one WhyChooseUs instance is allowed')
        super().save(*args, **kwargs)


class SocialMediaPost(models.Model):
    """Social media posts with embed codes"""
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('linkedin', 'LinkedIn'),
    ]
    
    title = models.CharField(max_length=200, help_text="Post title for admin reference")
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    embed_code = models.TextField(
        help_text="Paste the full iframe embed code from Facebook/Instagram/YouTube (e.g., <iframe src='...'></iframe>)"
    )
    post_url = models.URLField(
        blank=True,
        help_text="Direct link to the post (optional, for fallback)"
    )
    order = models.IntegerField(default=0, help_text="Display order (lower numbers first)")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Social Media Post"
        verbose_name_plural = "Social Media Posts"

    def __str__(self):
        return f"{self.platform.title()} - {self.title}"


class HomePage(models.Model):
    """Homepage content (singleton) - All text content for the homepage"""
    
    # Split Hero Section - Accounting Panel
    accounting_tag = models.CharField(max_length=100, default="Financial Services")
    accounting_title = models.CharField(max_length=200, default="Accounting & Tax Solutions")
    accounting_description = models.TextField(
        default="Expert bookkeeping, financial analysis, tax planning, and compliance management to keep your business financially sound and regulation-ready."
    )
    accounting_features = models.JSONField(
        default=list,
        help_text='List of features for accounting panel. Example: [{"icon": "BookOpen", "text": "Bookkeeping"}, {"icon": "TrendingUp", "text": "Financial Analysis"}]'
    )
    accounting_button1_text = models.CharField(max_length=50, default="Accounting Services")
    accounting_button1_link = models.CharField(max_length=200, default="/accounting")
    accounting_button2_text = models.CharField(max_length=50, default="Tax Services")
    accounting_button2_link = models.CharField(max_length=200, default="/tax")
    
    # Split Hero Section - IT Panel
    it_tag = models.CharField(max_length=100, default="Technology Solutions")
    it_title = models.CharField(max_length=200, default="IT & Digital Transformation")
    it_description = models.TextField(
        default="Strategic IT consulting, cybersecurity, cloud solutions, and digital marketing to accelerate your business into the future."
    )
    it_features = models.JSONField(
        default=list,
        help_text='List of features for IT panel. Example: [{"icon": "Code", "text": "Software Dev"}, {"icon": "Lock", "text": "Cybersecurity"}]'
    )
    it_button1_text = models.CharField(max_length=50, default="IT Services")
    it_button1_link = models.CharField(max_length=200, default="/it")
    it_button2_text = models.CharField(max_length=50, default="Digital Services")
    it_button2_link = models.CharField(max_length=200, default="/digital")
    
    # Middle Hero Section (with image)
    hero_title = models.CharField(
        max_length=300,
        default="The Remote and Physical Business Consultancy With All Related IT Services"
    )
    hero_subtitle = models.CharField(
        max_length=300,
        default="Professional consultancy to drive business growth and profitability"
    )
    hero_image = models.ImageField(
        upload_to='homepage/',
        blank=True,
        null=True,
        help_text="Hero section image (defaults to proforma-office.jpg if not set)"
    )
    hero_features = models.JSONField(
        default=list,
        help_text='List of hero features. Example: [{"text": "Expert Consultants"}, {"text": "Proven Solutions"}, {"text": "24/7 Support"}]'
    )
    
    # Meta
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Homepage Content"
        verbose_name_plural = "Homepage Content"

    def __str__(self):
        return "Homepage Content"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and HomePage.objects.exists():
            raise ValueError('Only one HomePage instance is allowed')
        super().save(*args, **kwargs)



class Project(models.Model):
    """Projects/Portfolio items"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/')
    client_name = models.CharField(max_length=200, blank=True)
    project_date = models.DateField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, help_text="e.g., Web Development, Accounting, IT Solutions")
    technologies = models.JSONField(default=list, blank=True, help_text="List of technologies used")
    project_url = models.URLField(blank=True, help_text="Live project URL")
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class HomePageService(models.Model):
    """Homepage services cards"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    icon_name = models.CharField(max_length=50, help_text="Lucide icon name (e.g., Calculator, Monitor, Shield)")
    image = models.ImageField(upload_to='homepage_services/')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Homepage Service"
        verbose_name_plural = "Homepage Services"

    def __str__(self):
        return self.title
