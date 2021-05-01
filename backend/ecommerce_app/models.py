from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Order(models.Model):
    payer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    paid = models.BooleanField(default=False)

    def __str__(self):
        return "{}:{}".format(self.id, self.payer.email)

    def item_name(self):
        return f"Order {self.id}"
