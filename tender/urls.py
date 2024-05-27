from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Router oluştur
router = DefaultRouter()
router.register(r'countries', CountriesView)
router.register(r'subscribers', SubscriberView)
router.register(r'projects-centers', ProjectsCenterView)
router.register(r'projects', ProjectsView)
router.register(r'anouncements', AnouncementView)
router.register(r'orders', OrderView)
router.register(r'partners', PartnersView)
router.register(r'anouncement-reports', AnouncementReportsView)
router.register(r'anouncer-files', AnouncerFilesView)

urlpatterns = [
    path('', include(router.urls)),
]
