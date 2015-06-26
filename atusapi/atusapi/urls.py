"""atusapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from api import views as api_views
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"respondents", api_views.RespondentsViewSet, base_name='respondents')
router.register(r"activity", api_views.ActivityViewSet)
router.register(r"person", api_views.PeopleViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace ='rest_framework')),
    # url(r'^respondents/(?P<pk>\d+)/activity-list/$', views.)
    # url(r'^respondents/activity-list')
    url(r'^householdlist/$', api_views.HouseholdListView.as_view(), name='householdlist'),
    url(r'^householdlist/(?P<pk>\d+)/$', api_views.HouseholdListDetailView.as_view(), name='householdlist-detail'),
]
