from rest_framework import serializers
from django.conf import settings
from .models import Order
from django.contrib.auth import get_user_model

User = get_user_model()


class BuyPremiumSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = User.objects.first()

    item_name = serializers.CharField(read_only=True)
    business = serializers.SerializerMethodField(read_only=True)
    amount = serializers.SerializerMethodField(read_only=True)
    invoice = serializers.SerializerMethodField(read_only=True)
    currency_code = serializers.SerializerMethodField(read_only=True)

    def get_business(self, obj):
        return settings.PAYPAL_RECEIVER_EMAIL

    def get_amount(self, obj):
        return str(settings.PREMIUM_COST)

    def get_invoice(self, obj):
        return obj.id

    def get_currency_code(self, obj):
        return "USD"

    def create(self, validated_data):
        return Order.objects.create(payer=self.user)
