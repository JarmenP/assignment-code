from django.urls import path
from .views import WeatherList, Yield
urlpatterns = [
    path('WeatherList/', WeatherList.as_view(), name='weather'),
    path("yeild/", Yield.as_view(), name='yeild'),
    path("status/", WeatherList.as_view(), name='status')
    ]