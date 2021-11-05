from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.TestAPIView.as_view()),
    # path('second/', views.RedirectAPIView.as_view()),

]