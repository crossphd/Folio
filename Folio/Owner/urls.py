from django.conf.urls import url
import Owner.views


urlpatterns = [
    url(r'$', Owner.views.home),
]
