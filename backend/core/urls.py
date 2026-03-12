from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ServiceViewSet, TeamMemberViewSet, InsightViewSet,
    SliderImageViewSet, CompanyStatViewSet, ContactInquiryViewSet,
    CompanyInfoViewSet, ProformaCardViewSet, CoreValueViewSet,
    WorkEnvironmentImageViewSet, WhyChooseUsViewSet, SocialMediaPostViewSet,
    HomePageViewSet, ProjectViewSet, HomePageServiceViewSet
)

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'team', TeamMemberViewSet, basename='team')
router.register(r'insights', InsightViewSet, basename='insight')
router.register(r'slider', SliderImageViewSet, basename='slider')
router.register(r'stats', CompanyStatViewSet, basename='stats')
router.register(r'contact', ContactInquiryViewSet, basename='contact')
router.register(r'company-info', CompanyInfoViewSet, basename='company-info')
router.register(r'proforma-cards', ProformaCardViewSet, basename='proforma-card')
router.register(r'core-values', CoreValueViewSet, basename='core-value')
router.register(r'work-environment', WorkEnvironmentImageViewSet, basename='work-environment')
router.register(r'why-choose-us', WhyChooseUsViewSet, basename='why-choose-us')
router.register(r'social-posts', SocialMediaPostViewSet, basename='social-post')
router.register(r'homepage', HomePageViewSet, basename='homepage')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'homepage-services', HomePageServiceViewSet, basename='homepage-service')

urlpatterns = [
    path('', include(router.urls)),
]
