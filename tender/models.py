from django.db import models
from django.contrib.auth.models import User

Rol = (
    ('admin', 'Administrador'),
    ('subscribers', 'subscribers'),
    ('anouncer','anouncer'),
)
Open_time =(
    ('09:00', '09:00'),
    ('10:00', '10:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
)

# class User(AbstractUser):
#     rol = models.CharField(choices=Rol, max_length=50)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class Countries(models.Model):
    name = models.CharField(max_length=100)
    fullname = models.CharField(max_length=255)
    alpha2 = models.CharField(max_length=2)
    alpha3 = models.CharField(max_length=3)

class Subscribers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    middlename = models.CharField(max_length=255)
    companyname = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    companyountry = models.ForeignKey(Countries, on_delete=models.CASCADE)
    division = models.CharField(max_length=255)
    postalcode = models.CharField(max_length=255)
    town = models.CharField(max_length=100)
    addressline1 = models.CharField(max_length=255)
    addressline2 = models.CharField(max_length=255)
    addressline3 = models.CharField(max_length=255)
    remembertoken = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProjectsCenters(models.Model):
    name = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

class Projects(models.Model):
    name = models.CharField(max_length=50)
    projectscenter = models.ForeignKey(ProjectsCenters, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

class Anouncements(models.Model):
    name = models.CharField(max_length=255)
    numberoflots = models.IntegerField()
    projectid = models.ForeignKey(Projects, on_delete=models.CASCADE)
    projectcenteranouncement = models.ForeignKey(ProjectsCenters, on_delete=models.CASCADE)
    typeofprocurement = models.CharField(max_length=255)
    procurementmethod = models.CharField(max_length=255)
    tenderowner = models.CharField(max_length=255)
    tendertitle = models.CharField(max_length=255)
    price = models.FloatField()
    opendate = models.DateField()
    opentime = models.CharField(choices=Open_time, max_length=50)
    anouncementpublicfile = models.CharField(max_length=255)
    anouncementprivatefile = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

class Orders(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    anouncement = models.ManyToManyField(Anouncements)
    responsesecuritysubmite = models.CharField(max_length=50)
    discount = models.FloatField()
    discountdol = models.FloatField()
    discounteuro = models.FloatField()
    total = models.FloatField()
    totaldol = models.FloatField()
    totaluro = models.FloatField()
    vat = models.FloatField()
    vatdol = models.FloatField()
    vateuro = models.FloatField()
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

class Partners(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    leader = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

class AnouncementReports(models.Model):
    anouncement = models.ManyToManyField(Anouncements)
    path = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

class AnouncerFiles(models.Model):
    project = models.ManyToManyField(Projects)
    type = models.IntegerField()
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)

class Favorites(models.Model):
    user = models.ManyToManyField(User)
    anouncement = models.OneToOneField(Anouncements, on_delete=models.CASCADE)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now_add=True)

class Lots(models.Model):
    order = models.OneToOneField(Orders, on_delete=models.CASCADE)
    lotnumber = models.IntegerField()
    title = models.CharField(max_length=255)
    discount = models.FloatField()
    discountdol = models.FloatField()
    discounteuro = models.FloatField()
    total = models.FloatField()
    totaldol = models.FloatField()
    totaleuro = models.FloatField()
    vat = models.FloatField()
    vatdol = models.FloatField()
    vateuro = models.FloatField()
    responsesecuritysubmited = models.CharField(max_length=255)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now_add=True)

class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

class OrderFiles(models.Model):
    order_id = models.ManyToManyField(Orders)
    path = models.CharField(max_length=50)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now_add=True)

class Payments(models.Model):
    anouncement = models.ForeignKey(Anouncements, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paymentfile = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now_add=True)
