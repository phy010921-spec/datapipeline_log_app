from django.contrib import admin
from django.urls import path, include
from ajaxapp.views import ajax_index, ajax_test, visualization,line,pie, getChartdata

app_name = "ajax_app"

urlpatterns = [
    path('', ajax_index, name="ajax_index"),
    path("ajax_test/", ajax_test, name="ajax_test"),
    path("visualization/", visualization, name="visualization"),
    path("visualization/line/", line, name="line"),
    path("visualization/pie/", pie, name="pie"),
    path("visualization/getChartdata/", getChartdata, name="getChartdata")

]