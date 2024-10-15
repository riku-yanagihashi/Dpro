import datetime
import uuid
from django.db import models

# Create your models here.
class VTDlog(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING)
    amount = models.IntegerField('amount')
    trade_id = models.UUIDField('trade_id', editable=False, null=True)
    description = models.CharField(max_length=150, default="")
    timestamp = models.DateTimeField(default=datetime.datetime.now())

class VTD(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, primary_key=True)
    value = models.IntegerField('amount')
    updated_at = models.DateTimeField(auto_now=True)

class AppClaims(models.Model):
    app_name = models.CharField('app_name', max_length=200)
    target_user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='target_user')
    amount = models.IntegerField('amount')
    created_at = models.DateTimeField(default=datetime.datetime.now())

class Claims(models.Model):
    from_user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING, related_name='from_user')
    to_user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING, related_name='to_user')
    amount = models.IntegerField('amount')
    created_at = models.DateTimeField(default=datetime.datetime.now())

class Messages(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    message = models.TextField()
    readed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=datetime.datetime.now())

class Trades(models.Model):
    trade_id = models.UUIDField('trade_id', unique=True, editable=False)
    from_user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING, related_name='trade_from_user')
    to_user = models.ForeignKey('accounts.User', on_delete=models.DO_NOTHING, related_name='trade_to_user')
    amount = models.IntegerField('amount')
    timestamp = models.DateTimeField(default=datetime.datetime.now())