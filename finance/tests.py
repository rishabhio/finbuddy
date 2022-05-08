from rest_framework.test import RequestsClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

# Create your tests here.
from .views import add_txn, list_txns, update_txn
from accounts.models import User
from finance.models import Transaction

"""

factory = APIRequestFactory()
user = User.objects.get(username='olivia')
view = AccountDetail.as_view()

# Make an authenticated request to the view...
request = factory.get('/accounts/django-superstars/')
force_authenticate(request, user=user)
response = view(request)

"""


class FinanceTests(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create(
            email="test@finbuddy.com",
            is_active=True,
            first_name="Tim",
            last_name="John",
        )
        self.lender = User.objects.create(
            email="lender@finbuddy.com",
            is_active=True,
            first_name="Lender",
            last_name="IO",
        )
        self.borrower = User.objects.create(
            email="borrower@finbuddy.com",
            is_active=True,
            first_name="Borrower",
            last_name="IO",
        )
        self.txn = Transaction.objects.create(
            lender=self.lender,
            borrower=self.borrower,
            amount=10000.00,
            reason="testing",
        )

    def test_list_txns(self):
        request = self.factory.get("/txns/")
        force_authenticate(request, user=self.user)
        resp = list_txns(request)
        assert resp.status_code == 200
        assert len(resp.data.get("result")) == 1
        assert resp.data.get("message") == "Results fetched successfully!"

    def test_add_txn(self):
        request = self.factory.post(
            "/txns/",
            {"borrower": 2, "amount": 12000.00, "reason": "Buying a new car"},
            format="json",
        )
        force_authenticate(request, user=self.user)
        resp = add_txn(request)
        assert resp.status_code == 201
        assert resp.data.get("message") == "Money lend note added successfully!"

    def test_mark_paid_txn(self):
        request = self.factory.patch("/txns/", {"txn_id": 1}, format="json")
        force_authenticate(request, user=self.lender)
        resp = update_txn(request)
        assert resp.status_code == 200
        assert resp.data.get("message") == "Money lend marked as paid!"
