from django.urls import path
from .views import ProductAPIView,ProductAPIDetails,product_searchList,image_view
from .ShopView import ShopAPIDetails, ShopContactDetailsAPI, ShopContactDetailsAPIView, ShopDetailsAPIView
urlpatterns = [
    path('productDetails', ProductAPIView.as_view()),
    path('productDetails/<int:id>', ProductAPIDetails.as_view()),
    path('productSearch/<str:productname>', product_searchList),
    path('showimage', image_view),
    path('shopDetails', ShopDetailsAPIView.as_view()),
    path('shopDetails/<int:id>', ShopAPIDetails.as_view()),
    path('shopContactDetails', ShopContactDetailsAPIView.as_view()),
    path('shopContactDetails/<int:id>', ShopContactDetailsAPI.as_view()),

    
    #path('details/<int:pk>/', article_details),
    #path('article', article_list),
]