from django.shortcuts import render

import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from correlations.serializers import CurrencyDataSerializer
from correlations.models import CurrencyData
import re
from datetime import datetime, date, timedelta
import time
import calendar

class CorrelationView(APIView):

    def get(self, request):
        try:
            coins = json.loads(request.GET["coins"]).lower()
            coins = re.findall(r'\w+', coins)
            time_from = json.loads(request.GET["time_from"])
            time_to = json.loads(request.GET["time_to"])
            date_from = datetime.fromtimestamp(time_from).date()
            date_to = datetime.fromtimestamp(time_to).date()
        except:
            return Response({"message": "attribute error"}, status=status.HTTP_400_BAD_REQUEST)
        delta = date_to - date_from  # as timedelta
        days = []
        for i in range(delta.days + 1):
            days.append(calendar.timegm((date_from + timedelta(days=i)).timetuple()))
        result = {}
        for day in days:
            try:
                data_by_day = CurrencyDataSerializer(CurrencyData.objects.get(timestamp=day)).data
            except:
                 return Response({"message": "can not retrieve the results"}, status=status.HTTP_400_BAD_REQUEST)
            coins_correlations = {}
            for coin in coins:
                coin_correlation = {}
                for other_coin in coins:
                    if other_coin == coin:
                        continue
                    coin_correlation[other_coin] = data_by_day["data"][coin]["close"]/data_by_day["data"][other_coin]["close"]
                    coins_correlations[coin] = coin_correlation
            result[day] = coins_correlations

        response = {"correlations": result}

        return Response(response, status=status.HTTP_200_OK)