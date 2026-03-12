from django.contrib import admin
from django import forms
from .models import (
    Service, TeamMember, Insight, SliderImage, 
    CompanyStat, ContactInquiry, CompanyInfo, ProformaCard,
    CoreValue, WorkEnvironmentImage, WhyChooseUs, SocialMediaPost, HomePage, Project,
    HomePageService
)
from .widgets import ContentBlocksWidget
import json


class ContentBlocksField(forms.CharField):
    """Custom field for content blocks that works with ContentBlocksWidget"""
    
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = ContentBlocksWidget()
        super().__init__(*args, **kwargs)
    
    def prepare_value(self, value):
        """Convert value to format expected by widget"""
        if value is None:
            return []
        if isinstance(value, str):
            try:
                return json.loads(value)
            except:
                return []
        return value
    
    def to_python(self, value):
        """Convert widget value to Python object"""
        if not value:
            return []
        if isinstance(value, str):
            try:
                return json.loads(value)
            except:
                return []
        return value


class InsightAdminForm(forms.ModelForm):
    content_blocks = ContentBlocksField(required=False)
    
    class Meta:
        model = Insight
        fields = '__all__'


class ProformaCardAdminForm(forms.ModelForm):
    content_blocks = ContentBlocksField(required=False)
    
    class Meta:
        model = ProformaCard
        fields = '__all__'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'short_description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'icon_name', 'color', 'order', 'is_active'),
            'description': 'Basic service information for the card display'
        }),
        ('Card Content', {
            'fields': ('short_description', 'features', 'image'),
            'description': 'Content shown on the service cards in the services list page'
        }),
        ('Detail Page - Hero Section', {
            'fields': ('hero_title', 'hero_subtitle'),
            'description': 'Hero section content for the service detail page'
        }),
        ('Detail Page - Main Content', {
            'fields': ('full_description', 'detail_content', 'services_list', 'detail_image'),
            'description': 'Main content for the service detail page'
        }),
    )
    
    class Media:
        css = {
            'all': ('admin/css/service_admin.css',)
        }
        js = ('admin/js/service_admin.js',)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'email', 'order', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'position', 'email']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']


@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    form = InsightAdminForm
    list_display = ['title', 'category', 'author', 'published_date', 'is_featured', 'is_published']
    list_filter = ['is_published', 'is_featured', 'category', 'published_date']
    search_fields = ['title', 'excerpt', 'author']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_featured', 'is_published']
    date_hierarchy = 'published_date'
    ordering = ['-published_date']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'excerpt', 'category', 'author', 'read_time')
        }),
        ('Content', {
            'fields': ('content_blocks',),
            'description': '<strong>Build your article content using the visual editor below.</strong> Add paragraphs, headings, and lists with the dropdown interface.'
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Publishing', {
            'fields': ('published_date', 'is_published', 'is_featured')
        }),
        ('Legacy Fields (Optional)', {
            'fields': ('introduction', 'content_sections', 'conclusion', 'content'),
            'classes': ('collapse',)
        }),
    )


@admin.register(SliderImage)
class SliderImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'subtitle']
    list_editable = ['order', 'is_active']
    ordering = ['order']


@admin.register(CompanyStat)
class CompanyStatAdmin(admin.ModelAdmin):
    list_display = ['label', 'value', 'suffix', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['label']
    list_editable = ['order', 'is_active', 'value']
    ordering = ['order']


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'subject', 'is_read', 'is_responded', 'created_at']
    list_filter = ['is_read', 'is_responded', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'subject', 'message']
    list_editable = ['is_read', 'is_responded']
    readonly_fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'message', 'created_at']
    ordering = ['-created_at']
    
    def has_add_permission(self, request):
        return False


@admin.register(ProformaCard)
class ProformaCardAdmin(admin.ModelAdmin):
    form = ProformaCardAdminForm
    list_display = ['title', 'slug', 'icon_name', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'icon_name']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'icon_name')
        }),
        ('Content', {
            'fields': ('content_blocks',),
            'description': '<strong>Build your card content using the visual editor below.</strong> Add paragraphs, headings, and lists with the dropdown interface.'
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email', 'phone', 'updated_at']
    readonly_fields = ['updated_at']
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not CompanyInfo.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_name', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'icon_name')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(WorkEnvironmentImage)
class WorkEnvironmentImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'image')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(WhyChooseUs)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ['partner_title', 'updated_at']
    readonly_fields = ['updated_at']
    
    fieldsets = (
        ('Key Advantages', {
            'fields': ('key_advantages',),
            'description': 'Enter key advantages as a list. Example: ["Deep understanding of Nepali business", "Experienced team of professionals", "Personalized solutions"]'
        }),
        ('Trusted Partner Section', {
            'fields': ('partner_title', 'partner_description'),
            'description': 'Main content for the "Your Trusted Partner" section'
        }),
        ('Numbered Points', {
            'fields': ('numbered_points',),
            'description': 'Enter numbered points as a list of objects. Example: [{"title": "Expert Guidance", "description": "Professional advice from experienced consultants"}, {"title": "Innovative Solutions", "description": "Cutting-edge approaches to business challenges"}]'
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not WhyChooseUs.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SocialMediaPost)
class SocialMediaPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'platform', 'is_active', 'order', 'created_at']
    list_filter = ['platform', 'is_active', 'created_at']
    search_fields = ['title', 'post_url']
    list_editable = ['is_active', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'platform', 'order', 'is_active')
        }),
        ('Embed Code', {
            'fields': ('embed_code',),
            'description': '<strong>Paste the full iframe embed code here.</strong><br>'
                         'For Facebook: Go to your post → Click "..." → Embed → Copy the iframe code<br>'
                         'For Instagram: Use Instagram\'s embed feature to get the iframe code<br>'
                         'For YouTube: Go to video → Share → Embed → Copy the iframe code'
        }),
        ('Fallback Link (Optional)', {
            'fields': ('post_url',),
            'description': 'Direct link to the post (optional, used as fallback if embed fails)'
        }),
    )



@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ['hero_title', 'is_active', 'updated_at']
    readonly_fields = ['updated_at', 'created_at']
    
    fieldsets = (
        ('Split Hero - Accounting Panel', {
            'fields': (
                'accounting_tag',
                'accounting_title',
                'accounting_description',
                'accounting_features',
                'accounting_button1_text',
                'accounting_button1_link',
                'accounting_button2_text',
                'accounting_button2_link',
            ),
            'description': 'Content for the left panel (Accounting & Tax Services)'
        }),
        ('Split Hero - IT Panel', {
            'fields': (
                'it_tag',
                'it_title',
                'it_description',
                'it_features',
                'it_button1_text',
                'it_button1_link',
                'it_button2_text',
                'it_button2_link',
            ),
            'description': 'Content for the right panel (IT & Digital Services)'
        }),
        ('Middle Hero Section', {
            'fields': (
                'hero_title',
                'hero_subtitle',
                'hero_image',
                'hero_features',
            ),
            'description': 'Content for the middle hero section with image'
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not HomePage.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        return False



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'client_name', 'is_featured', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'is_featured', 'category', 'created_at']
    search_fields = ['title', 'description', 'client_name', 'category']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_featured', 'is_active', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'category')
        }),
        ('Project Details', {
            'fields': ('client_name', 'project_date', 'technologies', 'project_url')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Display Settings', {
            'fields': ('order', 'is_featured', 'is_active')
        }),
    )



@admin.register(HomePageService)
class HomePageServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon_name', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'subtitle']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'title']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'subtitle', 'icon_name')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )
