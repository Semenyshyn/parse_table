from django.conf.urls import url
from . import views

app_name = 'parse_app'
urlpatterns = [
    url(r'^$', views.parse_url),
]