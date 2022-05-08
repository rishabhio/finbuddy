from django.db import models
from django.conf import settings
from .conf import TxnType

# Create your models here.
class Transaction(models.Model):
    """
    Transaction ID - STRING
    Transaction Type - STRING
    Transaction Date - DATE
    Transaction Status- STRING
    Transaction From -  STRING
    Transaction With -  STRING
    Reason - STRING
    """

    amount = models.DecimalField(
        "Amount", max_digits=19, decimal_places=3, default=0.000
    )
    reason = models.TextField("Long Description", null=True, blank=True)
    created_at = models.DateTimeField("created_on", auto_now_add=True)
    updated_at = models.DateTimeField("updated_on", auto_now=True)
    lender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="lender",
    )
    borrower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="borrower",
    )
    paid_back = models.BooleanField("Status", default=False)

    def __str__(self):
        return str(self.lender) + "->" + str(self.borrower)
