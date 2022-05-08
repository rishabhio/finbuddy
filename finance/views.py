from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def list_txns(request):
    return Response({"result": {}, "message": "Not implemented yet!"})


@api_view(["POST"])
def add_txn(request):
    return Response({"result": {}, "message": "Not implemented yet!"})


@api_view(["PATCH", "PUT"])
def update_txn(request):
    return Response({"result": {}, "message": "Not implemented yet!"})
