from django.db import models

# Create your models here.
from mongoengine import Document, EmbeddedDocument, fields


class CurrencyDataInput(EmbeddedDocument):
    timestamp = fields.IntField(required=True)
    data = fields.DictField(required=True)
    # conversionType = fields.StringField(required=True)
    # time = fields.IntField(required=True)
    # close = fields.FloatField(required=True)
    # volumefrom = fields.FloatField(required=True)
    # conversionSymbol = fields.StringField(required=True)
    # open = fields.FloatField(required=True)
    # low = fields.FloatField(required=True)
    # high = fields.FloatField(required=True)
    # volumeto = fields.FloatField(required=True)
    meta = {'collection': 'currency'}


class CurrencyData(Document):
    timestamp = fields.IntField(required=True)
    data = fields.DictField(required=True)
    # conversionType = fields.StringField(required=True)
    # time = fields.IntField(required=True)
    # close = fields.FloatField(required=True)
    # volumefrom = fields.FloatField(required=True)
    # conversionSymbol = fields.StringField(required=True)
    # open = fields.FloatField(required=True)
    # low = fields.FloatField(required=True)
    # high = fields.FloatField(required=True)
    # volumeto = fields.FloatField(required=True)
    meta = {'collection': 'currency'}

