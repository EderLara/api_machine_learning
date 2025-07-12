from django.urls import path
from .views import RFView

urlpatterns = [
    path("random_forest/", RFView.as_view(), name='random_forest'),
]