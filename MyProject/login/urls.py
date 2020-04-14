from django.urls import path
from .views import LoginAPIView,SignUpView

urlpatterns = [
    path('checkLogin', LoginAPIView.as_view()),
    path('signup', SignUpView.as_view())
    #path('details/<int:pk>/', article_details),
    #path('article', article_list),
]