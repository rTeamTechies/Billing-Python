from django.urls import path
from .views import ArticleDetails, ArticleAPIView,article_details, article_list

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('details/<int:id>/', ArticleDetails.as_view()),
    #path('details/<int:pk>/', article_details),
    #path('article', article_list),
]