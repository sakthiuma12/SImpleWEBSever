from django.urls import path
from first_app import views
url patterns=[
    path('',views.home),
]