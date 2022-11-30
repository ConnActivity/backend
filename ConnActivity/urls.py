"""ConnActivity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

import start.views
from start import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start.views.index, name='index'),
    path('events/', views.event_list),
    path('events/<int:pk>', views.event_detail),
    path('user/', views.user_list),
    path('user/<str:pk>', views.user_detail),
    path('join_event/<int:pk>', views.join_event),
    path('leave_event/<int:pk>', views.leave_event),
    path('approve_member_wait_list/<int:pk>/<str:member>', views.approval_member_wait_list),
    path('tag/', views.tags),
    path('delete_tag/<int:pk>', views.tags_delete),
    path('list_user_with_events/<str:pk>', views.user_list_events),
    path('list_user_with_events_wait_list/<str:pk>', views.user_list_events_wait_list),
]
urlpatterns = format_suffix_patterns(urlpatterns)
