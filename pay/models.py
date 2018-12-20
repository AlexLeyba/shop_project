from django.contrib.auth.models import User
from django.db import models


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=99, decimal_places=2)


class AdminWallet(models.Model):
    balance = models.DecimalField(max_digits=99, decimal_places=2)
    percent = models.IntegerField(default=20)


class History(models.Model):
    ACTION = (
        ('1', 'покупка'),
        ('2', 'продажа'),
        ('3', 'пополнение'),
    )
    user = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    action = models.CharField(choices=ACTION, max_length=1, default='1')
    balance = models.IntegerField(default=0)
    history = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)



