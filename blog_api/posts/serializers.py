from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        # fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post
        fields = '__all__'
        read_only_fields = ['author']

    def validate(self, attrs):
        attrs['author'] = self.context['request'].user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)


class CommentSerializer(serializers.ModelSerializer):
    # post = serializers.SerializerMethodField()
    # post = serializers.ReadOnlyField(source='post.title',read_only=False)
    name = serializers.ReadOnlyField(source='name.username')

    class Meta:
        model = Comment
        fields = ('id','post', 'name', 'body', 'date_added')
        # read_only_fields = ['name']

    def validate(self, attrs):
        attrs['name'] = self.context['request'].user
        return attrs

    # def get_post(self, obj):
    #     return PostSerializer(obj.post).data