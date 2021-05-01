from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import serializers
from .models import Order


class BuyPremium(mixins.CreateModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = serializers.BuyPremiumSerializer
    queryset = Order.objects.all()
    permission_classes = [
        IsAuthenticated
    ]

    @action(methods=['post'], detail=False)
    def buy_premium(self, request):
        return self.create(request)

    @action(methods=['post'], detail=False)
    def payment_done(self, request):
        self.request.user.profile.is_premium = True
        self.request.user.profile.save()
        return Response(status=status.HTTP_200_OK)
