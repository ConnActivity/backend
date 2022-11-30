from rest_framework import serializers

from .models import Event, User, Tag


class PrivateMemberOrOpenEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'date_published', 'date', 'location', 'description', 'member_limit',
                  'image', 'tags', 'creator']


class PrivateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'date_published', 'date', 'description', 'member_limit', 'image', 'tags', 'creator']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'gender', 'user_email', 'user_age', 'university', 'user_bio', 'user_tags']


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'gender', 'user_age', 'university', 'user_bio', 'user_tags']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'value']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'date_published', 'date', 'location', 'description', 'member_limit', 'image', 'tags',
                  'member_list', 'is_private', 'member_wait_list', 'creator']
