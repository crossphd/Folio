from django.shortcuts import render

from app.models import Portfolio, Stock, PortfolioStock

from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    assert isinstance(request, HttpRequest)

    portfolios = Portfolio.objects.portfolios_for_user(request.user)
    stocks = PortfolioStock.objects.stocks_for_user(request.user)

    return render(
        request,
        'Owner/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'portfolios': portfolios,
            'stocks': stocks,
        }
    )