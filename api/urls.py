from django.urls import URLPattern, path
from .views.parts import PartsView, PartView

urlpatterns = [
    path('part/', PartsView.as_view(), name='parts'),
    path('part/<int:pk>', PartView.as_view(), name='part'),
]