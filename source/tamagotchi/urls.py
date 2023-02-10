from django.urls import path
from tamagotchi.views.base import index_view
from tamagotchi.views.cat_stats import cat_stats_view

urlpatterns = [
    path('', index_view),
    path('cat_stats/', cat_stats_view)
]
