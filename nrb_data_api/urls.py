from django.urls import path
from . import views

urlpatterns = [
    path('bio-data/',views.BioDataList.as_view(),),
    path('bio-data/<int:pk>/',views.BioDataDetail.as_view()),
    path('address/',views.AddressList.as_view(),),
    path('address/<int:pk>/',views.AddressDetail.as_view()),
]
