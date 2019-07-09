from django.contrib import admin
from app.models import Stock, Portfolio, PortfolioStock

class StockAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'symbol', 'price', 'dividend_yield', 'update_date')

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'owner', 'pub_date')

class PortfolioStockAdmin(admin.ModelAdmin):
    list_display = ('id', 'portfolio', 'stock', 'shares', 'add_date', 'update_date')

admin.site.register(Stock, StockAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioStock, PortfolioStockAdmin)
    