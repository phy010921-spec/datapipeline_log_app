from django.urls import path,include
from conf.views import index
from log import views

app_name = "log_app"

urlpatterns = [
    path('',views.log_index, name="log_index"),
    path("log_gen_i/", views.log_gen_i, name = "log_gen_i"),
    path("btn_gen_i_click/<int:product_id>",views.btn_gen_i_click, name="btn_gen_i_click" ),
    path("log_gen_ii/", views.log_gen_ii, name="log_gen_ii"),  #-->{% url "log_app:log_gen_ii" %}
    path("btn_gen_ii_click/", views.btn_gen_ii_click, name="btn_gen_ii_click"),
    path("btn_gen_iii_click/", views.btn_gen_iii_click, name="btn_gen_iii_click"),
    path("btn_openapi/", views.btn_openapi, name="btn_openapi"),
    path("btn_openapi_click/", views.btn_openapi_click, name="btn_openapi_click")

]