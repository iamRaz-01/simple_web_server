from django.urls import path
from .views import systemInfo

urlpatterns = [
    path('', systemInfo, name='system_info'),
]
