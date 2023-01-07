from django.core.paginator import Paginator
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ConnActivity.auth_user import user_auth
from start.models import Event
from start.models import Tag
from start.models import User
from start.serializers import EventSerializer
from start.serializers import TagSerializer
from start.serializers import UserSerializer, PrivateEventSerializer, PrivateMemberOrOpenEventSerializer, \
    MemberSerializer


# TODO: Check if everything is working
# Create your views here.
def index(request):
    return HttpResponse("Henlo world. You're at the start index.")


def get_user_serializer_class(userid, user):
    if userid == user.user_id:
        return UserSerializer(user)
    else:
        return MemberSerializer(user)


@api_view(['GET', 'POST'])
def user_list(request, order="username", format=None):
    """
    Create a new user or get user list
    """
    userid = user_auth(request.COOKIES.get("user_token"))
    if request.method == 'GET':
        return Response(status=status.HTTP_418_IM_A_TEAPOT)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data.update(user_id=userid)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # ?TODO: Datenrückgabe wegmachen
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    userid = user_auth(request.COOKIES.get("user_token"))
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = get_user_serializer_class(userid, user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid() and userid == user.user_id:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        if userid == user.user_id:
            user.delete()
        return Response(status=status.HTTP_200_OK)


def get_event_serializer_class(userid, event):
    if userid == event.creator_id:
        return EventSerializer(event)
    elif event.member_list.filter(user_id=userid).exists() or not event.is_private:
        return PrivateMemberOrOpenEventSerializer(event)
    elif event.is_private:
        return PrivateEventSerializer(event)


@api_view(['GET', 'POST'])
def event_list(request, format=None):
    """List all events or create new"""
    userid = user_auth(request.COOKIES.get("user_token"))
    page = request.GET.get("page", 1)
    order = request.GET.get("order", "-date_published")
    if request.method == 'GET':
        event = Event.objects.all().order_by(order)
        serializer = PrivateEventSerializer(event, many=True)
        paginator = Paginator(serializer.data, 10)
        headers = {"Link": paginator.num_pages}
        return Response(paginator.page(page).object_list, headers=headers)

    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid() and userid == request.data.get('creator') and userid == request.data.get(
                'member_list'):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'PUT', 'DELETE'])
def event_detail(request, pk, format=None):
    """Retrieve, update or delete a code snippet"""
    userid = user_auth(request.COOKIES.get("user_token"))

    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = get_event_serializer_class(userid, event)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
def join_event(request, pk):
    userid = user_auth(request.COOKIES.get("user_token"))
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if event.is_private and event.member_list.count() < event.member_limit:
        event.member_wait_list.add(userid)
        return Response(status=status.HTTP_100_CONTINUE)
    elif event.member_list.count() < event.member_limit:
        event.member_list.add(userid)
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response('User konnte nicht hinzugefügt werden')


@api_view(['PUT'])
def leave_event(request, pk):
    userid = user_auth(request.COOKIES.get("user_token"))
    try:
        # The Owner can't leave the event
        if Event.objects.get(pk=pk).creator_id == userid:
            return Response(status=status.HTTP_403_FORBIDDEN)
        event = Event.objects.get(pk=pk)
        event.member_list.remove(userid)
        return Response(status=status.HTTP_200_OK)
    except Event.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def approval_member_wait_list(request, pk, member):
    userid = user_auth(request.COOKIES.get("user_token"))
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if event.creator_id == userid:
        try:
            if event.member_list.count() < event.member_limit:
                event.member_wait_list.remove(member)
                event.member_list.add(member)
        except:
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        serializer = EventSerializer(event)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# TODO: Eventuell Tags mit User Rechten
# TODO: Keine doppelten Einträge ermöglichen

@api_view(['GET', 'POST'])
def tags(request):
    userid = user_auth(request.COOKIES.get("user_token"))

    if request.method == 'GET':
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def tags_delete(request, pk):
    userid = user_auth(request.COOKIES.get("user_token"))
    if userid == 'qZeeNMtw55d0rkkgg87ImP7EhTV2':
        try:
            tag = Tag.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            tag.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def user_list_events(request, pk):
    user_auth(request.COOKIES.get("user_token"))
    try:
        events = Event.objects.filter(member_list=pk)
        serializer = PrivateEventSerializer(events, many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def user_list_events_wait_list(request, pk):
    user_auth(request.COOKIES.get("user_token"))
    try:
        events = Event.objects.filter(member_wait_list=pk)
        serializer = PrivateEventSerializer(events, many=True)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
