from datetime import date, datetime, timedelta
from typing import List

import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework.views import APIView

from brmed.highcharts.utils.vatcomply import VatComplyRequest
from brmed.highcharts.api.v1.serializers import GraphSerializer
from brmed.highcharts.utils.convert_date_str import convert_date_to_str, convert_str_to_date

class HighchartsAPIView(APIView):
    def get(self, request: Request) -> Response:
        start_date: str = request.GET.get('start_date', None)
        end_date: str = request.GET.get('end_date', None)
        serializer = GraphSerializer(data={
            "start_date": start_date,
            "end_date": end_date
        })

        data: dict = {
            "BRL": [],
            "EUR": [],
            "JPY": [],
        }
        if serializer.is_valid():
            responses: List[requests.Response] = VatComplyRequest().main(date_start=start_date, date_end=end_date)
            start_date: date = convert_str_to_date(start_date)
            end_date: date = convert_str_to_date(end_date)

            data["start_date"] = {
                "day": start_date.day,
                "month": start_date.month,
                "year": start_date.year
            }
            data["end_date"] = {
                "day": end_date.day,
                "month": end_date.month,
                "year": end_date.year
            }
        else:
            end_date: date = (datetime.now().date() - timedelta(days=1))
            start_date: date = (end_date - timedelta(days=5))

            responses: List[requests.Response] = VatComplyRequest().main(date_start=convert_date_to_str(start_date), date_end=convert_date_to_str(end_date))

            data["start_date"] = {
                "day": start_date.day,
                "month": start_date.month,
                "year": start_date.year
            }
            data["end_date"] = {
                "day": end_date.day,
                "month": end_date.month,
                "year": end_date.year
            }

        for response in responses:
            if response.status_code == status.HTTP_200_OK:
                data["BRL"].append(response.json().get('rates').get("BRL"))
                data["EUR"].append(response.json().get('rates').get("EUR"))
                data["JPY"].append(response.json().get('rates').get("JPY"))

        end_date: date = (datetime.now().date() - timedelta(days=1))
        start_date: date = (end_date - timedelta(days=5))
        data["start_date"] = {
            "day": start_date.day,
            "month": start_date.month,
            "year": start_date.year
        }
        data["end_date"] = {
            "day": end_date.day,
            "month": end_date.month,
            "year": end_date.year
        }
        return Response(data)
