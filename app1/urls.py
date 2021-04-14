from django.urls import path
from app1 import views

app_name='aap1'

urlpatterns = [
    path("app/",views.index,name='map'),
    path("front/<name>",views.front,name='map1'),
]
