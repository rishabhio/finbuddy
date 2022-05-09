# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User

# Create your views here.


@api_view(["GET"])
def user_details(request):
    me = request.user
    return Response(
        {
            "message": "User details fetched successfully!",
            "result": {"name": me.first_name, "email": me.email},
        }
    )


@api_view(["GET"])
def user_list(request):
    me = request.user
    users = User.objects.all().exclude(id=me.id).values("id", "first_name", "email")
    return Response({"message": "users fetched successfully!", "result": users})
