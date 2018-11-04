from django.urls import path
from new_shop.views import *

urlpatterns = [
    path('', General.as_view()),
    path('category/<slug:slug>/', Category_View.as_view(), name="category"),
    path('product/<int:slug>/', Product_View.as_view(), name="product"),
    path('card/', Card_View.as_view(), name="card"),
    path('add_to_card/<int:slug>/', AddCardItem.as_view(), name='add_to_card'),
    path('delete_card_item/<int:slug>/', DeleteCardItem.as_view(), name='delete_card_item'),
    path('profile/', ProfileView.as_view(), name='profile')
]
