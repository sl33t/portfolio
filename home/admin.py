from django.contrib import admin

from home.models import PortfolioItem

admin_model = [PortfolioItem]

for item in admin_model:
    admin.site.register(item)
