from . import views
from django.urls import include, path

urlpatterns = [
    path('player/<str:gsis_id>/', views.player_page, name='player-page'),
]