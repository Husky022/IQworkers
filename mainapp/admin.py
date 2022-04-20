from django.contrib import admin


# Register your models here.
from portfolioapp.models import PortfolioObject, PortfolioImage
from .models import Client

admin.site.register(PortfolioObject)
admin.site.register(PortfolioImage)
admin.site.register(Client)

