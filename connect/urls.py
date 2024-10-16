
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TweetViewSet, CommentViewSet, ReplyViewSet
from .import views

router = DefaultRouter()
router.register(r'tweets', TweetViewSet)    
router.register(r'comments', CommentViewSet) 
router.register(r'replies', ReplyViewSet)   


urlpatterns = [
    path('', include(router.urls)),  
]
