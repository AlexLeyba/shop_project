from django.urls import path
from new_shop.views import *


urlpatterns = [
    path('', General.as_view()),
    path('category/<slug:slug>/', Category_View.as_view(), name="category"),
    path('product/<int:slug>/', Product_View.as_view(), name="product"),
    path('card-item/', AddCardItem.as_view(), name="addcarditem"),
]