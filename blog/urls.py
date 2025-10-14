from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("posts/<slug:slug>/", views.post_detail, name="post_detail"),
    path("events/<int:event_id>/", views.event_detail, name="event_detail"),
]