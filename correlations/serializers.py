from correlations.models import CurrencyData
from rest_framework_mongoengine import serializers


class CurrencyDataSerializer(serializers.DocumentSerializer):
    class Meta:
        model = CurrencyData
        fields = '__all__'
