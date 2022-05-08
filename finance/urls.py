from django.urls import path
from .views import add_txn, list_txns, update_txn

urlpatterns = [
    # path("", SomePage.as_view(), name="some_name"),
    path("", list_txns, name="list_txns"),
    path("", add_txn, name="add_txn"),
    path("", update_txn, name="update_txn"),
]
