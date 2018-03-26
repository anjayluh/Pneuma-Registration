from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import datetime
from django.contrib import admin
class Visitor(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name =models.CharField(max_length = 25)
    country = CountryField()
    address = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    phone_number = models.PositiveIntegerField()
    email = models.EmailField(max_length = 255)
    date_of_visit = datetime.date.today()

    class Meta:
        db_table = "Visitors"

    def __unicode__(self):
        return self.Visitor.first_name
class Reception(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'country', 'address', 'date_of_birth', 'phone_number',
	'email', 'date_of_visit')
	fields = ['first_name', 'last_name', 'country', 'date_of_visit']