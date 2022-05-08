from django.urls import path
from .views import add_txn

urlpatterns = [
    # path("", SomePage.as_view(), name="some_name"),
    path("", add_txn, name="add_txn")
]
