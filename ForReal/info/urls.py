from django.urls import path
from .views import *

urlpatterns = [
    path('', news_home, name="info_home"),
    path('create', create, name="create"),
    path('<int:pk>', NewsDetailView.as_view(), name ="info-detail")]