from django.conf.urls import include, url
from rest_framework import routers
from . import views

# create api routers
apiurls = [
    url(r'^$', views.main),
    # url(r'^login/$', views.login),
    # url(r'^logout/$', views.logout),
]