from django.urls import path
from .views import ProductAPIView,ProductAPIDetails,product_searchList

urlpatterns = [
    path('productDetails', ProductAPIView.as_view()),
    path('productDetails/<int:id>/', ProductAPIDetails.as_view()),
    path('productSearch/<str:productname>', product_searchList),

    
    #path('details/<int:pk>/', article_details),
    #path('article', article_list),
]