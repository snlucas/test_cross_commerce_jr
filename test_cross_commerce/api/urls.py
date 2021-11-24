from django.urls import path

from .views import ListData


urlpatterns = [
    path('', ListData.as_view()),
]
