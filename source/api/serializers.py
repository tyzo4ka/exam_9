from webapp.models import Photography, Like, User, Comments
from rest_framework import serializers


class CommentsSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comments
        fields = ('id', 'text', 'photography', "comments_author", 'created_date')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'photography', "like_author", 'like')
