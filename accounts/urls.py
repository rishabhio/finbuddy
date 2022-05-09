from django.urls import path
from .views import user_details, user_list

urlpatterns = [
    # path("", SomePage.as_view(), name="some_name"),
    path("details/", user_details, name="user_details"),
    path("list/", user_list, name="user_list"),
]
