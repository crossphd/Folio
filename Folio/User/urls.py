from django.conf.urls import url
import User.views


urlpatterns = [
    url(r'$', User.views.home),
]
