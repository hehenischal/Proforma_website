from rest_framework import serializers
from .models import (
    Service, TeamMember, Insight, SliderImage,
    CompanyStat, ContactInquiry, CompanyInfo, ProformaCard,
    CoreValue, WorkEnvironmentImage, WhyChooseUs, SocialMediaPost, HomePage, Project,
    HomePageService
)


class ServiceSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    detail_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Service
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
    
    def get_detail_image(self, obj):
        if obj.detail_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.detail_image.url)
            return obj.detail_image.url
        return None


class TeamMemberSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = TeamMember
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class InsightSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Insight
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class InsightListSerializer(serializers.ModelSerializer):
    """Lighter serializer for list views"""
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Insight
        fields = ['id', 'title', 'slug', 'excerpt', 'image', 'category', 
                  'author', 'read_time', 'published_date', 'is_featured']
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class SliderImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = SliderImage
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class CompanyStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStat
        fields = '__all__'


class ContactInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInquiry
        fields = ['first_name', 'last_name', 'email', 'phone', 'subject', 'message']
        
    def create(self, validated_data):
        return ContactInquiry.objects.create(**validated_data)


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = '__all__'


class ProformaCardSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = ProformaCard
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None



class CoreValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoreValue
        fields = '__all__'


class WorkEnvironmentImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = WorkEnvironmentImage
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class WhyChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUs
        fields = '__all__'


class SocialMediaPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaPost
        fields = ['id', 'title', 'platform', 'embed_code', 'post_url', 'order', 'created_at']



class HomePageSerializer(serializers.ModelSerializer):
    hero_image = serializers.SerializerMethodField()
    
    class Meta:
        model = HomePage
        fields = '__all__'
    
    def get_hero_image(self, obj):
        if obj.hero_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.hero_image.url)
            return obj.hero_image.url
        return None



class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Project
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None



class HomePageServiceSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = HomePageService
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None
