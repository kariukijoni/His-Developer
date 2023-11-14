from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from cities_light.models import Country
from cities_light.models import City

# Create your models here.

class Address(models.Model):
    postal_address=models.TextField(max_length=100)
    postal_code=models.IntegerField()


class BioData(models.Model):
    HONORIFICS=(('Prof','Prof'),
             ('Dr','Dr'),
             ('Mr','Mr'),
             ('Mrs','Mrs'),
             ('Miss','Miss'),
             ('Ms','Ms'),
             ('Rev','Rev'))
    
    GENDER=(('MALE','MALE'),
            ('FEMALE','FEMALE'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=10,choices=HONORIFICS)
    date_of_birth=models.DateTimeField(max_length=8)
    id_number=models.IntegerField()
    gender=models.CharField(max_length=10,choices=GENDER)
    nationality = models.ForeignKey(Country,max_length=50, on_delete=models.SET_NULL, null=True, blank=True,related_name='country_name') 
    ethnicity=models.CharField(max_length=50)
    home_county = models.ForeignKey(City, max_length=50, on_delete=models.SET_NULL, null=True, blank=True,related_name='city_name')
    posta_address=models.ForeignKey(Address,max_length=100, on_delete=models.SET_NULL,null=True,related_name='town_name')
    town_city= models.ForeignKey(City,max_length=100,  on_delete=models.SET_NULL, null=True, blank=True)
    telephone_number = models.CharField(null=True, max_length=100, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    mobile_number = models.CharField(null=True, max_length=100, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])
    email_address=models.EmailField()
    alternative_contact_person=models.CharField(max_length=50)
    altenative_contact_person_telephone_number = models.CharField(null=True, max_length=100, validators=[RegexValidator(r'^\d{3}-\d{3}-\d{4}$')])


  
