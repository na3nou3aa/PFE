from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    # path('activate/<uid64>/token', views.activate, name="activate"),
    path('scan_list', views.scanlist, name="scan_list"),

    path('create-scan/', views.createScan, name="create-scan"),
    path('asset_discovery/', views.Asset_Discovery, name="asset_discovery"),
    path('network_list/', views.NetworkList, name="network_list"),
    path('details/', views.consult, name="details"),
    path('web_formatter/', views.web_formatter, name="web_formatter"),
]
