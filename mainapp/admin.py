from django.contrib import admin


# Register your models here.
from portfolioapp.models import PortfolioObject, PortfolioImage, PortfolioFunctions

admin.site.register(PortfolioObject)
admin.site.register(PortfolioImage)
admin.site.register(PortfolioFunctions)
