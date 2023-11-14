from django.contrib import admin
from.models import Address,BioData

# Register your models here.
model_list=[Address,BioData]
admin.site.register(model_list)