from django.urls import path
from . import views

app_name = 'car'
urlpatterns = [
    path('details/<int:id>/', views.CarDetailView.as_view(), name='car_details'),
    path('buy/<int:id>/', views.buy_now, name='buy_now'),
]