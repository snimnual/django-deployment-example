from django.urls import path
from basic_app import views
from django.conf.urls import url
# FOR TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]
