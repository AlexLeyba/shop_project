from django.urls import path
from new_shop.views import *

urlpatterns = [
    path('', General.as_view()),
    path('category/<slug:slug>/', Category_View.as_view(), name="category"),
    path('product/<int:slug>/', Product_View.as_view(), name="product"),
    path('card/', Card_View.as_view(), name="card"),
    path('add_to_card/<int:slug>/', AddCardItem.as_view(), name='add_to_card'),
    path('delete_card_item/<int:slug>/', DeleteCardItem.as_view(), name='delete_card_item'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('zacaz/', ZacazView.as_view(), name='zacaz'),
    path('search/', SearchView.as_view(), name='search'),
    path('comments/<int:slug>', CommentVeiw.as_view(), name='comments'),
    path('sendcomment/<int:pk>/', SendCommentVeiw.as_view(), name='sendcomment'),
    path('sell/', Create.as_view(), name='sell'),
    path('update/<int:pk>', Update.as_view(), name='update'),
    path('user-product/', UserProduct.as_view(), name='userproduct'),
    path('rating/<int:pk>/<int:slug>/', RatingVeiw.as_view(), name='rating'),


]
