from django.urls import path
from .views import DemmandList, DemmandDetail, AddressList


urlpatterns = [
    path('demmands/', DemmandList.as_view()),
    path('demmands/<int:pk>/', DemmandDetail.as_view()),
    path('address/', AddressList.as_view()),
]
