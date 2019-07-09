from django.shortcuts import render

from app.models import Portfolio, Stock, PortfolioStock

from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    assert isinstance(request, HttpRequest)

    portfolios = Portfolio.objects.filter(owner=request.user)
    stocks = PortfolioStock.objects.filter(portfolio__owner=request.user)

    return render(
        request,
        'User/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'portfolios': portfolios,
        }
    )
