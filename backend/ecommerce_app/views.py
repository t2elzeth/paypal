from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from .models import Order


@login_required()
def index(request):
    return render(request, "ecommerce_app/index.html")


class BuyPremium(mixins.CreateModelMixin,
                 viewsets.GenericViewSet):
    serializer_class = serializers.BuyPremiumSerializer
    queryset = Order.objects.all()

    @action(methods=['post'], detail=False)
    def buy_premium(self, request):
        return self.create(request)

    @action(methods=['post'], detail=False)
    def payment_done(self, request):
        self.request.user.profile.is_premium = True
        self.request.user.profile.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def payment_cancelled(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def payment_done(request):
    return render(request, 'ecommerce_app/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'ecommerce_app/payment_cancelled.html')
