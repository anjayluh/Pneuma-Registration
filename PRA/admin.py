from django.contrib import admin
from .models import Visitor, Reception

#admin.site.register(Visitor)
@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    pass
