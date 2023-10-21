from django.db import models
from django.utils import timezone

from apps.accounts.models import Account


class Auction(models.Model):
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    recipient = models.CharField(Account, null=True, blank=True, max_length=32)
    item_name = models.CharField(max_length=32)
    quantity = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    cost_gold = models.IntegerField()
    cost_rubies = models.IntegerField()
    item_type = models.CharField(max_length=16)
    item_rarity = models.CharField(max_length=16)
