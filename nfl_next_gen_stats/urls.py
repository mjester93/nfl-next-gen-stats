from . import views
from django.urls import include, path

urlpatterns = [
    # Regular Views
    path('', views.home, name='home'),
    path('player-search/', views.SearchResultsView.as_view(), name='player-search'),
    path('player/<str:gsis_id>/', views.player_page, name='player-page'),
    path('player/<str:gsis_id>/<int:season>/', views.player_page, name='player-season'),

    # API Views
    path('api/qb-ngs-stats/<int:season>/', views.qb_ngs_api, name='qb-api'),
    path('api/wr-ngs-stats/<int:season>/<int:week>/', views.wr_ngs_api, name='wr-api'),
]