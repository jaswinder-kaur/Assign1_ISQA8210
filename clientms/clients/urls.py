from django.urls import path
from .import views


from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    VehicleListView,
    VehicleUpdateView,
    VehicleDeleteView,
    VehicleCreateView

)


urlpatterns = [
    path('', views.ClientListView.as_view(), name='client_list'),
    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('vehicle', views.VehicleListView.as_view(), name='vehicle_list'),
    path('vehicle/new/', VehicleCreateView.as_view(), name='vehicle_new'),
    path('vehicle/<int:pk>/edit/', VehicleUpdateView.as_view(), name='vehicle_edit'),
    path('vehicle/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle_delete'),

]
