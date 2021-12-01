
from django.urls import path
from .views import article_list , article_detail,ArticlesAPIView,ArticlesDetail, GenericAPIView,GenAPIView


urlpatterns = [
    
    path('article/', article_list),
    path('detail/<int:pk>/', article_detail),
    path('articles/',ArticlesAPIView.as_view()),
    path('Detail/<int:id>/', ArticlesDetail.as_view()),
    path('generics/',GenericAPIView.as_view()),
    path('delete/<int:id>/',GenAPIView.as_view()),
  
]   