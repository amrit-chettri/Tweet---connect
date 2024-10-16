from .models import Tweet ,Comment , Reply
from rest_framework import serializers


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('user', 'content', 'Images', 'created_at')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields =('content', 'tweet', 'user', 'created_at', 'updated_at')        


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ('content', 'comment', 'user', 'created_at', 'updated_at')  

