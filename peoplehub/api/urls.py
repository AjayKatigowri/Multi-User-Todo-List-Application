from django.urls import path
from .import views

urlpatterns = [
    path('singleobj/<int:pk>/',views.SingleObjAPIView.as_view()),
    path('multiobj/',views.MultiObjAPIView.as_view()),
]
