from rest_framework.serializers import ModelSerializer
from .models import *


class CountriesSerializer(ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'

class SubscriberSerializer(ModelSerializer):
    class Meta:
        model = Subscribers
        fields = '__all__'


class ProjectsCenterSerializer(ModelSerializer):
    class Meta:
        model = ProjectsCenters
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class AnouncementSerializer(ModelSerializer):
    class Meta:
        model = Anouncements
        fields = '__all__'

    
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'

class AnouncementReportsSerializer(ModelSerializer):
    class Meta:
        model = AnouncementReports
        fields = '__all__'

    
class AnouncerFileSerializer(ModelSerializer):
    class Meta:
        model = AnouncerFiles
        fields = '__all__'
    
class FavoritesSerializer(ModelSerializer):
    class Meta:
        model = Favorites
        fields = '__all__' 
    
class LotSerializer(ModelSerializer):
    class Meta:
        model = Lots
        fields = '__all__'

    
class MigrationSerializer(ModelSerializer):
    class Meta:
        model = Migrations
        fields = '__all__'


class OrderFilesSerializer(ModelSerializer):
    class Meta:
        model = OrderFiles
        fields = '__all__'

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'

