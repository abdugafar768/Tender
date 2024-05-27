from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class CountriesView(ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class SubscriberView(ModelViewSet):
    queryset = Subscribers.objects.all()
    serializer_class = SubscriberSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ProjectsCenterView(ModelViewSet):
    queryset = ProjectsCenters.objects.all()
    serializer_class = ProjectsCenterSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ProjectsView(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    
class AnouncementView(ModelViewSet):
    queryset = Anouncements.objects.all()
    serializer_class = AnouncementSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class OrderView(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    

class PartnersView(ModelViewSet):
    queryset = Partners.objects.all()
    serializer_class = PartnerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class AnouncementReportsView(ModelViewSet):
    queryset = AnouncementReports.objects.all()
    serializer_class = AnouncementReportsSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]



class AnouncerFilesView(ModelViewSet):
    queryset = AnouncerFiles.objects.all()
    serializer_class = AnouncerFileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


