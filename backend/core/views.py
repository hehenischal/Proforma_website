from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import (
    Service, TeamMember, Insight, SliderImage,
    CompanyStat, ContactInquiry, CompanyInfo, ProformaCard,
    CoreValue, WorkEnvironmentImage, WhyChooseUs, SocialMediaPost, HomePage, Project,
    HomePageService
)
from .serializers import (
    ServiceSerializer, TeamMemberSerializer, InsightSerializer,
    InsightListSerializer, SliderImageSerializer, CompanyStatSerializer,
    ContactInquirySerializer, CompanyInfoSerializer, ProformaCardSerializer,
    CoreValueSerializer, WorkEnvironmentImageSerializer, WhyChooseUsSerializer,
    SocialMediaPostSerializer, HomePageSerializer, ProjectSerializer,
    HomePageServiceSerializer
)


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for services"""
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'


class TeamMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for team members"""
    queryset = TeamMember.objects.filter(is_active=True)
    serializer_class = TeamMemberSerializer
    permission_classes = [AllowAny]


class InsightViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for insights/blog posts"""
    queryset = Insight.objects.filter(is_published=True)
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.action == 'list':
            return InsightListSerializer
        return InsightSerializer
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured insights"""
        featured = self.queryset.filter(is_featured=True)[:3]
        serializer = InsightListSerializer(featured, many=True)
        return Response(serializer.data)


class SliderImageViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for slider images"""
    queryset = SliderImage.objects.filter(is_active=True)
    serializer_class = SliderImageSerializer
    permission_classes = [AllowAny]


class CompanyStatViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for company statistics"""
    queryset = CompanyStat.objects.filter(is_active=True)
    serializer_class = CompanyStatSerializer
    permission_classes = [AllowAny]


class ContactInquiryViewSet(viewsets.ModelViewSet):
    """API endpoint for contact inquiries"""
    queryset = ContactInquiry.objects.all()
    serializer_class = ContactInquirySerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']  # Only allow POST
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {'message': 'Your inquiry has been submitted successfully!'},
            status=status.HTTP_201_CREATED
        )


class CompanyInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for company information"""
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['get'])
    def current(self, request):
        """Get current company info"""
        try:
            company_info = CompanyInfo.objects.first()
            serializer = self.get_serializer(company_info)
            return Response(serializer.data)
        except CompanyInfo.DoesNotExist:
            return Response(
                {'error': 'Company information not found'},
                status=status.HTTP_404_NOT_FOUND
            )


class ProformaCardViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Proforma cards (Vision, Mission, Benefits, etc.)"""
    queryset = ProformaCard.objects.filter(is_active=True)
    serializer_class = ProformaCardSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'


class CoreValueViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for core values"""
    queryset = CoreValue.objects.filter(is_active=True)
    serializer_class = CoreValueSerializer
    permission_classes = [AllowAny]


class WorkEnvironmentImageViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for work environment images"""
    queryset = WorkEnvironmentImage.objects.filter(is_active=True)
    serializer_class = WorkEnvironmentImageSerializer
    permission_classes = [AllowAny]


class WhyChooseUsViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Why Choose Us content"""
    queryset = WhyChooseUs.objects.all()
    serializer_class = WhyChooseUsSerializer
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['get'])
    def current(self, request):
        """Get current Why Choose Us content"""
        try:
            content = WhyChooseUs.objects.first()
            serializer = self.get_serializer(content)
            return Response(serializer.data)
        except WhyChooseUs.DoesNotExist:
            return Response(
                {'error': 'Why Choose Us content not found'},
                status=status.HTTP_404_NOT_FOUND
            )



class SocialMediaPostViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Social Media Posts"""
    queryset = SocialMediaPost.objects.filter(is_active=True)
    serializer_class = SocialMediaPostSerializer
    permission_classes = [AllowAny]



class HomePageViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Homepage content"""
    queryset = HomePage.objects.filter(is_active=True)
    serializer_class = HomePageSerializer
    permission_classes = [AllowAny]
    
    @action(detail=False, methods=['get'])
    def current(self, request):
        """Get current homepage content"""
        try:
            homepage = HomePage.objects.filter(is_active=True).first()
            if not homepage:
                return Response(
                    {'error': 'Homepage content not found'},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = self.get_serializer(homepage, context={'request': request})
            return Response(serializer.data)
        except HomePage.DoesNotExist:
            return Response(
                {'error': 'Homepage content not found'},
                status=status.HTTP_404_NOT_FOUND
            )



class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Projects"""
    queryset = Project.objects.filter(is_active=True)
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """Get featured projects"""
        featured = self.queryset.filter(is_featured=True)[:6]
        serializer = self.get_serializer(featured, many=True, context={'request': request})
        return Response(serializer.data)



class HomePageServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for Homepage Services"""
    queryset = HomePageService.objects.filter(is_active=True)
    serializer_class = HomePageServiceSerializer
    permission_classes = [AllowAny]
