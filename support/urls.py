from support.views import *
from django.urls import path

urlpatterns = [
    path('support/', HelpView.as_view(), name='help'),
    path('helpform/', HelpForm.as_view(), name="send_form"),
]
