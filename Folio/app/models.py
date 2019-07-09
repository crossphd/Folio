"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Stock(models.Model):
    text = models.CharField(max_length=200)
    symbol = models.CharField(max_length=10)
    price = models.FloatField()
    dividend_yield = models.FloatField()
    dividend_amount = models.FloatField()
    update_date = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return "{0}({1})".format(self.text, self.symbol)

class Portfolio(models.Model):
    text = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name="portfolio_owner")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{0} - {1}".format(self.owner, self.text)

class PortfolioStock(models.Model):
    stock = models.ForeignKey(Stock)
    portfolio = models.ForeignKey(Portfolio)
    update_date = models.DateTimeField(auto_now=True)
    add_date = models.DateTimeField(auto_now_add=True)
    shares = models.IntegerField(default=0)
    
    def value(self):
        return shares * self.stock.price
        
    def annual_dividend(self):
        return shares * self.stock.dividend_amount

    def __str__(self):
        return "{0} - {1}".format(self.portfolio, self.stock)
    