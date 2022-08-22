from django.urls import URLPattern, path
from .views.parts import PartsView, PartView

urlpatterns = [
    path('parts/', PartsView.as_view(), name='parts'),
    path('parts/<int:pk>', PartView.as_view(), name='part'),
]