from django.urls import path
from .views import ProductAPIView,ProductAPIDetails

urlpatterns = [
    path('productDetails', ProductAPIView.as_view()),
    path('productDetails/<int:id>/', ProductAPIDetails.as_view()),
    #path('details/<int:pk>/', article_details),
    #path('article', article_list),
]