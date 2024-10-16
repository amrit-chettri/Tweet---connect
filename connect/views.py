from django.shortcuts import render
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from django.views.decorators.cache import cache_page
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Tweet, Comment, Reply
from .serializers import TweetSerializer , CommentSerializer , ReplySerializer

# Create your views here.


class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.select_related('user').all()
    serializer_class = TweetSerializer
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]  
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['created_at']



class TweetListView(APIView):
    @method_decorator(cache_page(60 * 15))  
    def get(self, request, *args, **kwargs):
        tweets = Tweet.objects.all()
        serialized_data = TweetSerializer(tweets, many=True).data
        return Response({"tweets": serialized_data})



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('user', 'tweet').all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]  



class CommentListView(APIView):
    @method_decorator(cache_page(60 * 15))  
    def get(self, request, *args, **kwargs):
        comments = Lead.objects.all()
        serialized_data = CommentSerializer(comments, many=True).data
        return Response({"comments": serialized_data})



class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.select_related('user', 'comment').all()
    serializer_class = ReplySerializer
    authentication_classes = [JWTAuthentication] 
    permission_classes = [IsAuthenticated]  



class ReplyListView(APIView):
    @method_decorator(cache_page(60 * 15))  
    def get(self, request, *args, **kwargs):
        replies = Reply.objects.all()
        serialized_data = ReplySerializer(replies, many=True).data
        return Response({"replies": serialized_data})
