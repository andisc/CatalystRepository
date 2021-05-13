from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('nasdaq_earnigs_reports/', views.nasdaq_earnigs_view, name='nasdaq_earnigs_view'),
    path('bio_catalysts/', views.bio_catalysts_view, name='bio_catalysts_view'),
    path('pre_market/', views.pre_market_view, name='pre_market_view'),
    path('privacy_policy/', views.privacy_policy_view, name='privacy_policy_view'),
    path('stock_details/<str:i_stock_ticker>/', views.stock_details_view, name='stock_details_view'),
    path('purgeLogging/', views.purgeLogging_view, name='purgeLogging_view'),
    path('teste/', views.teste_view, name='teste_view'),
]