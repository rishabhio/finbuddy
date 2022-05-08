from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, serializers
from .serializers import TxnSerializer
from .models import Transaction

# Create your views here.
@api_view(["GET"])
def list_txns(request):
    message = "Results fetched successfully!"
    status_code = status.HTTP_200_OK
    txns = Transaction.objects.all()
    serializer = TxnSerializer(txns, many=True)
    return Response({"result": serializer.data, "message": message})


@api_view(["POST"])
def add_txn(request):
    req_data = request.data
    req_data["lender"] = request.user.id
    txn_serializer = TxnSerializer(data=req_data)
    result = {}
    message = "Money lend note added successfully!"
    status_code = status.HTTP_201_CREATED

    if txn_serializer.is_valid(raise_exception=True):
        txn_serializer.save()
        result = txn_serializer.data

    return Response({"result": result, "message": message}, status=status_code)


@api_view(["PATCH", "PUT"])
def update_txn(request):
    txn_id = request.data.get("txn_id", None)
    try:
        txn = Transaction.objects.get(lender=request.user.id, id=txn_id)
        txn.paid_back = True
        txn.save()
    except ModuleNotFoundError:
        return Response({"Error": "Transaction does not exist!"})

    return Response({"result": {}, "message": "Money lend marked as paid!"})
