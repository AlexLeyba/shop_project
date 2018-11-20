from pay.views import *
from django.urls import path

urlpatterns = [
    path('auction/', Balance.as_view(), name='balance'),
    path('pay/<int:slug>', BayView.as_view(), name='bay'),
    path('history/', HistoryView.as_view(), name='history')
]
