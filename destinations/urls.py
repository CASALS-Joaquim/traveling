from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='destinations'),
    path('add', views.Add.as_view(), name='add_destination'),
    path('country/add', views.AddCountry.as_view(), name='add_country'),
    path('detail/<int:id>', views.Detail.as_view(), name='detail')
]