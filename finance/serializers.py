from rest_framework import serializers
from .models import Transaction


class TxnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["lender", "borrower", "amount", "reason"]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_amount(self, amount):
        """
        Check that the amount is valid
        """

        if amount < 100.00:
            raise serializers.ValidationError("Amount should be greater than 100.00")
        return amount

    def validate_reason(self, reason):
        """
        Check that the reason is stated.
        """
        if not reason:
            raise serializers.ValidationError("Please provide the reason for lending!")
        return reason

    def validate(self, obj):
        """
        Avoid lending to self.
        """
        if obj.get("lender") == obj.get("borrower"):
            raise serializers.ValidationError("Not possible to lend to self")
        return obj

    def create(self, validated_data):
        txn = Transaction(**validated_data)
        txn.save()
        return txn
