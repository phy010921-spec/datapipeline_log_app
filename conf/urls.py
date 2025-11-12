from django.contrib import admin
from django.urls import path,include
from conf.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',index),
    path('applog/',include('log.urls')),
    path('ajax/',include('ajaxapp.urls')),
]