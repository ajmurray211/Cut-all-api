from django.urls import URLPattern, path
from .views.parts import PartsView, PartView
from .views.worker import WorkersView, WorkerView

urlpatterns = [
    path('parts/', PartsView.as_view(), name='parts'),
    path('parts/<int:pk>', PartView.as_view(), name='part'),
    path('workers/', WorkersView.as_view(), name='workers'),
    path('workers/<int:pk>', WorkerView.as_view(), name='worker'),
]