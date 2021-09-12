from django.urls import path

from .views import *

urlpatterns = [
    path("<int:pk>/edit/", ClientUpdateView.as_view(), name="client_edit"),
    path("<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("<int:pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),
    path("new/", ClientCreateView.as_view(), name="client_new"),
    path("", ClientListView.as_view(), name="client_list"),
    path("<int:pk>/comment/new/", CommentCreateView.as_view(), name="comment_new"),
]
